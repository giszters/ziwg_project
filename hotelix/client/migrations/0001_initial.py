# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_auto_20141027_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('name', models.CharField(max_length=100, verbose_name='Imi\u0119 i nazwisko')),
                ('telephone', models.CharField(blank=True, max_length=20, verbose_name='nr tel.', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message="Numer tel. musi by\u0107 w formacie '+999999999'. Od 9 do 15. cyfr.")])),
                ('address', models.TextField(verbose_name='Adres', blank=True)),
                ('description', models.TextField(verbose_name='Opis', blank=True)),
            ],
            options={
                'verbose_name': 'Klient',
                'verbose_name_plural': 'Klienci',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_people', models.IntegerField(verbose_name='Liczba go\u015bci')),
                ('number_of_disabled', models.IntegerField(default=0, verbose_name='Liczba niepe\u0142nosprawnych')),
                ('arrival_time', models.DateTimeField(verbose_name='Data przyjazdu')),
                ('departure_time', models.DateTimeField(verbose_name='Data wyjazdu')),
                ('price_per_night', models.DecimalField(verbose_name='Cena za noc', max_digits=10, decimal_places=2)),
                ('client', models.ForeignKey(to='client.Client')),
                ('rooms', models.ManyToManyField(to='structure.Room')),
            ],
            options={
                'verbose_name': 'Zam\xf3wienie',
                'verbose_name_plural': 'Zam\xf3wienia',
            },
            bases=(models.Model,),
        ),
    ]
