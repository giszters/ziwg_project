# -*- coding: utf-8 -*-
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
