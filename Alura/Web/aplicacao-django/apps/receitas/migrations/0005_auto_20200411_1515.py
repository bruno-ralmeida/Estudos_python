# Generated by Django 3.0.5 on 2020-04-11 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_auto_20200411_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 11, 15, 15, 15, 499943)),
        ),
    ]
