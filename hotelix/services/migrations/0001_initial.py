# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateField(verbose_name='Data rozpocz\u0119cia')),
                ('stop_time', models.DateField(verbose_name='Data zako\u0144czenia')),
                ('order_time', models.TimeField(verbose_name='Godzina podania', blank=True)),
                ('price', models.DecimalField(verbose_name='Cena za obiad', max_digits=10, decimal_places=2)),
                ('client', models.ForeignKey(to='client.Client')),
            ],
            options={
                'verbose_name': 'Zam\xf3wienia dania',
                'verbose_name_plural': 'Zam\xf3wienia da\u0144',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nazwa dania')),
                ('description', models.TextField(verbose_name='Opis dania')),
            ],
            options={
                'verbose_name': 'Danie',
                'verbose_name_plural': 'Dania',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateField(verbose_name='Data rozpocz\u0119cia')),
                ('stop_time', models.DateField(verbose_name='Data zako\u0144czenia')),
                ('order_time', models.TimeField(verbose_name='Godzina us\u0142ugi', blank=True)),
                ('price', models.DecimalField(verbose_name='Cena za obiad', max_digits=10, decimal_places=2)),
                ('client', models.ForeignKey(to='client.Client')),
            ],
            options={
                'verbose_name': 'zam\xf3wienie us\u0142ugi',
                'verbose_name_plural': 'zam\xf3wienia us\u0142ug',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nazwa us\u0142ugi')),
                ('description', models.TextField(verbose_name='Opis')),
            ],
            options={
                'verbose_name': 'Us\u0142uga dot.',
                'verbose_name_plural': 'Us\u0142ugi dot.',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='service_type',
            field=models.ForeignKey(to='services.ServiceType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mealorder',
            name='meal_type',
            field=models.ForeignKey(to='services.MealType'),
            preserve_default=True,
        ),
    ]
