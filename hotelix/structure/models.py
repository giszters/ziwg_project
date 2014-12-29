# -*- coding: utf-8 -*-
import datetime
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(u"Nazwa budynku", max_length=50, null=False,
                            blank=False)

    class Meta:
        verbose_name = u"Budynek"
        verbose_name_plural = u"Budynki"

    def __unicode__(self):
        return u"%s) %s" % (self.id, self.name)

    def get_absolute_url(self):
        return reverse('structure:house_edit', kwargs={'pk': str(self.id)})


class Floor(models.Model):
    number = models.IntegerField(u"Numer piętra", null=False, blank=False)
    house = models.ForeignKey(House, null=False)

    class Meta:
        verbose_name = u"Piętro"
        verbose_name_plural = u"Piętra"

    def __unicode__(self):
        return u"%s) floor=%s" % (self.id, self.number)

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_absolute_url(self):
        return reverse('structure:floor_edit',
            kwargs={
                 'pk': str(self.id),
                 'house_id': str(self.house.id)
             }
        )


class Chamber(models.Model):
    description = models.TextField(u"Opis pomieszczenia", null=True)
    house = models.ForeignKey(House, null=False)

    class Meta:
        verbose_name = u"Pomieszczenie spec."
        verbose_name_plural = u"Pomieszczenia spec."

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_absolute_url(self):
        return reverse('structure:chamber_edit',
            kwargs={
                 'pk': str(self.id),
                 'house_id': str(self.house.id)
             }
        )


class Room(models.Model):
    beds = models.IntegerField(u"Liczba miejsc", null=False, blank=False)
    name = models.CharField(u"Nazwa", max_length=10, null=False, blank=False,
                            default='')
    for_disabled = models.BooleanField(u"Dla niepełnosprawnych", default=False)
    floor = models.ForeignKey(Floor, null=False)

    def __unicode__(self):
        return u"%s) floor=%s, name=%s beds=%s" %\
            (self.id, self.floor.number, self.name, self.beds)

    class Meta:
        verbose_name = u"Pokój"
        verbose_name_plural = u"Pokoje"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_absolute_url(self):
        return reverse('structure:room_edit',
            kwargs={
                 'pk': str(self.id),
                 'house_id': str(self.floor.house.id),
                 'floor_id': str(self.floor.id)
             }
        )

    def is_reserved(self, date):
        date_min = datetime.datetime.combine(date, datetime.time.min)
        date_max = datetime.datetime.combine(date, datetime.time.max)
        o1 = self.order_set.filter(arrival_time__lt=date_min)\
                           .filter(departure_time__gt=date_max)
        o2 = self.order_set.filter(arrival_time__contains=date)
        o3 = self.order_set.filter(departure_time__contains=date)
        bgcolor = ''
        first_half = False
        second_half = False
        order_id = 0
        # now is ugly, but echhh...
        if o1.count() > 0:
            bgcolor = o1[0].get_color()
            first_half = True
            second_half = True
            order_id = int(o1[0].id)
        elif o2.count() > 0:
            bgcolor = o2[0].get_color()
            first_half = False
            second_half = True
            order_id = int(o2[0].id)
        elif o3.count() > 0:
            bgcolor = o3[0].get_color()
            first_half = True
            second_half = False
            order_id = int(o3[0].id)
        """
        for order in (o1, o2, o3):
            if order.count() > 0:
                flag = True
                bgcolor = order[0].get_color()
        """
        return {
            'bgcolor': bgcolor,
            'first_half': first_half,
            'second_half': second_half,
            'order_id': order_id
        }
