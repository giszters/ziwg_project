# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20141110_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealorder',
            name='serving',
            field=models.DecimalField(default=1, verbose_name='Liczba porcji', max_digits=10, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mealorder',
            name='price',
            field=models.DecimalField(verbose_name='Cena za 1 porcje', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
