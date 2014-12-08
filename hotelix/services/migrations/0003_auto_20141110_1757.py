# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20141110_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealorder',
            name='order_time',
            field=models.TimeField(null=True, verbose_name='Godzina podania', blank=True),
            preserve_default=True,
        ),
    ]
