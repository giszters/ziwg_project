# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealorder',
            name='price',
            field=models.DecimalField(verbose_name='Cena za danie', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='order_time',
            field=models.TimeField(null=True, verbose_name='Godzina us\u0142ugi', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='price',
            field=models.DecimalField(verbose_name='Cena za us\u0142ug\u0119', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
