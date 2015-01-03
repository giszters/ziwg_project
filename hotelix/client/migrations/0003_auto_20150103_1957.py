# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_order_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Status', choices=[(0, 'zam\xf3wiony'), (1, 'zap\u0142acony'), (2, 'zameldowany')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(verbose_name='Klient', to='client.Client'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(null=True, verbose_name='Opis', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='rooms',
            field=models.ManyToManyField(to='structure.Room', verbose_name='Pokoje'),
            preserve_default=True,
        ),
    ]
