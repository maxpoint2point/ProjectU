from ProjectU.celery import app
from .models import Workplace
from .service import exchange as ex


@app.task
def exchange(pk):
    workplace = Workplace.objects.get(pk=pk)
    ex.main_exchange(workplace)
