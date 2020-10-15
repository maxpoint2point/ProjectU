# Generated by Django 3.1.1 on 2020-10-15 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UTMWatch', '0006_auto_20201015_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=36, verbose_name='Идентификатор')),
                ('date', models.DateTimeField()),
                ('type', models.CharField(choices=[('stock', '1 регистр'), ('shop', '2 регистр')], max_length=6, verbose_name='Тип остатков')),
                ('status', models.CharField(choices=[('loaded', 'Загружены'), ('send_ac', 'Передан в УТМ'), ('error', 'Ошибка')], max_length=10, verbose_name='Статус')),
                ('workplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UTMWatch.workplace')),
            ],
            options={
                'verbose_name': 'Документ с остатками',
                'verbose_name_plural': 'Документы с остатками',
            },
        ),
        migrations.CreateModel(
            name='StockPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('alcohol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UTMWatch.alcohol')),
                ('fa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UTMWatch.fa')),
                ('fb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UTMWatch.fb')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restheader_stockposition', to='UTMWatch.restheader')),
            ],
            options={
                'verbose_name': 'Остатки 1 регистр',
                'verbose_name_plural': 'Остатки 1 регистр',
            },
        ),
        migrations.CreateModel(
            name='ShopPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('alcohol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UTMWatch.alcohol')),
                ('rest_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restheader_shopposition', to='UTMWatch.restheader')),
            ],
            options={
                'verbose_name': 'Остатки 2 регистр',
                'verbose_name_plural': 'Остатки 2 регистр',
            },
        ),
    ]
