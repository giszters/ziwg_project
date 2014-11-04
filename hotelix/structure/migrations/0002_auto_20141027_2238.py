# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chamber',
            options={'verbose_name': 'Pomieszczenie', 'verbose_name_plural': 'Pomieszczenia'},
        ),
        migrations.AlterModelOptions(
            name='floor',
            options={'verbose_name': 'Pi\u0119tro', 'verbose_name_plural': 'Pi\u0119tra'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'Budynek', 'verbose_name_plural': 'Budynki'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Pok\xf3j', 'verbose_name_plural': 'Pokoje'},
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=b'', max_length=10, verbose_name='Nazwa'),
            preserve_default=True,
        ),
    ]
