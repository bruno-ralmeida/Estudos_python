# Generated by Django 3.0.5 on 2020-04-11 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 4, 11, 14, 43, 52, 300729)),
        ),
    ]
