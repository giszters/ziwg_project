# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_auto_20141027_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chamber',
            options={'verbose_name': 'Pomieszczenie spec.', 'verbose_name_plural': 'Pomieszczenia spec.'},
        ),
    ]
