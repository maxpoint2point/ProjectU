from json import loads

from django.forms.widgets import Select
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import pluralize
from django.contrib import admin, messages
from django import forms

from celery.utils import cached_property
from celery import current_app

from API.models import PeriodicTask, Tasks, PeriodicTasks


class TaskSelectWidget(Select):
    """Widget that lets you choose between task names."""

    celery_app = current_app
    _choices = None

    def tasks_as_choices(self):
        _ = self._modules  # noqa
        tasks = list(sorted(name for name in self.celery_app.tasks
                            if not name.startswith('celery.')))
        return (('', ''),) + tuple(zip(tasks, tasks))

    @property
    def choices(self):
        if self._choices is None:
            self._choices = self.tasks_as_choices()
        return self._choices

    @choices.setter
    def choices(self, _):
        # ChoiceField.__init__ sets ``self.choices = choices``
        # which would override ours.
        pass

    @cached_property
    def _modules(self):
        self.celery_app.loader.import_default_modules()


class TaskChoiceField(forms.ChoiceField):
    """Field that lets you choose between task names."""

    widget = TaskSelectWidget

    def valid_value(self, value):
        return True


class PeriodicTaskForm(forms.ModelForm):
    """Form that lets you create and modify periodic tasks."""

    regtask = TaskChoiceField(
        label=_('Task (registered)'),
        required=False,
    )
    task = forms.CharField(
        label=_('Task (custom)'),
        required=False,
        max_length=200,
    )

    class Meta:
        """Form metadata."""

        model = PeriodicTask
        exclude = ()

    def clean(self):
        data = super(PeriodicTaskForm, self).clean()
        regtask = data.get('regtask')
        if regtask:
            data['task'] = regtask
        if not data['task']:
            exc = forms.ValidationError(_('Need name of task'))
            self._errors['task'] = self.error_class(exc.messages)
            raise exc

        if data.get('expire_seconds') is not None and data.get('expires'):
            raise forms.ValidationError(
                _('Only one can be set, in expires and expire_seconds')
            )
        return data

    def _clean_json(self, field):
        value = self.cleaned_data[field]
        try:
            loads(value)
        except ValueError as exc:
            raise forms.ValidationError(
                _('Unable to parse JSON: %s') % exc,
            )
        return value

    def clean_args(self):
        return self._clean_json('args')

    def clean_kwargs(self):
        return self._clean_json('kwargs')


@admin.register(Tasks)
class Task(admin.ModelAdmin):
    form = PeriodicTaskForm
    celery_app = current_app
    date_hierarchy = 'start_time'
    list_display = ('__str__', 'enabled', 'interval', 'start_time',
                    'last_run_at', 'one_off')
    list_filter = ['enabled', 'one_off', 'task', 'start_time', 'last_run_at']
    actions = ('enable_tasks', 'disable_tasks', 'toggle_tasks', 'run_tasks')
    search_fields = ('name',)
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': ('name', 'regtask', 'task', 'enabled', 'description', 'workplace'),
            'classes': ('extrapretty', 'wide'),
        }),
        ('Schedule', {
            'fields': ('interval', 'crontab', 'solar', 'clocked',
                       'start_time', 'last_run_at', 'one_off'),
            'classes': ('extrapretty', 'wide'),
        }),
        ('Arguments', {
            'fields': ('args', 'kwargs'),
            'classes': ('extrapretty', 'wide', 'collapse', 'in'),
        }),
        # ('Execution Options', {
        #     'fields': ('expires', 'expire_seconds', 'queue', 'exchange',
        #                'routing_key', 'priority', 'headers'),
        #     'classes': ('extrapretty', 'wide', 'collapse', 'in'),
        # }),
    )
    readonly_fields = (
        'last_run_at',
    )

    def get_queryset(self, request):
        qs = super(Task, self).get_queryset(request)
        return qs.select_related('interval', 'crontab', 'solar', 'clocked')

    def enable_tasks(self, request, queryset):
        rows_updated = queryset.update(enabled=True)
        PeriodicTasks.update_changed()
        self._message_user_about_update(request, rows_updated, 'enabled')

    enable_tasks.short_description = _('Включить отмеченные задачи')

    def disable_tasks(self, request, queryset):
        rows_updated = queryset.update(enabled=False)
        PeriodicTasks.update_changed()
        self._message_user_about_update(request, rows_updated, 'disabled')

    disable_tasks.short_description = _('Отключить отмеченные задачи')

    def run_tasks(self, request, queryset):
        self.celery_app.loader.import_default_modules()
        tasks = [(self.celery_app.tasks.get(task.task),
                  loads(task.args),
                  loads(task.kwargs),
                  task.queue)
                 for task in queryset]

        if any(t[0] is None for t in tasks):
            for i, t in enumerate(tasks):
                if t[0] is None:
                    break

            # variable "i" will be set because list "tasks" is not empty
            not_found_task_name = queryset[i].task

            self.message_user(
                request,
                _('task "{0}" not found'.format(not_found_task_name)),
                level=messages.ERROR,
            )
            return

        task_ids = [task.apply_async(args=args, kwargs=kwargs, queue=queue)
                    if queue and len(queue)
                    else task.apply_async(args=args, kwargs=kwargs)
                    for task, args, kwargs, queue in tasks]
        tasks_run = len(task_ids)
        self.message_user(
            request,
            _('{0} task{1} {2} successfully run').format(
                tasks_run,
                pluralize(tasks_run),
                pluralize(tasks_run, _('was,were')),
            ),
        )

    run_tasks.short_description = _('Выполнить отмеченные задачи')
