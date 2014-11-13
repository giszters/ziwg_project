# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from client.models import Client


class MealType(models.Model):
    name = models.CharField(u"Nazwa dania", max_length=50, null=False)
    description = models.TextField(u"Opis dania", null=False)

    class Meta:
        verbose_name = u"Danie"
        verbose_name_plural = u"Dania"

    def __unicode__(self):
        return u"%s) %s" % (self.id, self.name)

    def get_absolute_url(self):
        return reverse('services:mealtype_edit', kwargs={'pk': str(self.id)})

    def get_delete_url(self):
        return reverse('services:mealtype_delete', kwargs={'pk': str(self.id)})

    def get_verbose_name(self):
        # return field Meta.verbose_name of this class
        return self._meta.verbose_name


class MealOrder(models.Model):
    meal_type = models.ForeignKey(MealType, null=False)
    start_time = models.DateField(u"Data rozpoczęcia", null=False)
    stop_time = models.DateField(u"Data zakończenia", null=False)
    order_time = models.TimeField(u"Godzina podania", blank=True, null=True)
    client = models.ForeignKey(Client, null=False)
    price = models.DecimalField(u"Cena za 1 porcje", null=False, max_digits=10,
                                decimal_places=2)
    serving = models.DecimalField(u"Liczba porcji", null=False, max_digits=10,
                                  decimal_places=1, default=1)

    class Meta:
        verbose_name = u"Zamówienia dania"
        verbose_name_plural = "Zamówienia dań"

    def __unicode__(self):
        return u"%s) meal: %s, client: %s" % (self.id, self.meal_type.name,
                                              self.client.name)
    
    def get_absolute_url(self):
        return reverse('services:mealorder_edit', kwargs={'pk': str(self.id)})

    def get_name(self):
        return u"%s - %s - %s" % (self.meal_type.name, self.client.name,
                                  self.price)

    def get_verbose_name(self):
        return self._meta.verbose_name


class ServiceType(models.Model):
    name = models.CharField(u"Nazwa usługi", max_length=50, null=False)
    description = models.TextField(u"Opis", null=False)

    class Meta:
        verbose_name = u"Usługa dot."
        verbose_name_plural = u"Usługi dot."

    def __unicode__(self):
        return u"%s) %s" % (self.id, self.name)

    def get_absolute_url(self):
        return reverse('services:servicetype_edit', kwargs={'pk': str(self.id)})

    def get_delete_url(self):
        return reverse('services:servicetype_delete', kwargs={'pk': str(self.id)})

    def get_verbose_name(self):
        return self._meta.verbose_name


class ServiceOrder(models.Model):
    service_type = models.ForeignKey(ServiceType, null=False)
    start_time = models.DateField(u"Data rozpoczęcia", null=False)
    stop_time = models.DateField(u"Data zakończenia", null=False)
    order_time = models.TimeField(u"Godzina usługi", blank=True, null=True)
    client = models.ForeignKey(Client, null=False)
    price = models.DecimalField(u"Cena za usługę", null=False, max_digits=10,
                                decimal_places=2)

    class Meta:
        verbose_name = u"Zamówienie usługi"
        verbose_name_plural = u"Zamówienia usług"

    def __unicode__(self):
        return u"%s) service: %s, client: %s" % (self.id, self.service_type.name,
                                                 self.client.name)

    def get_absolute_url(self):
        return reverse('services:serviceorder_edit', kwargs={'pk': str(self.id)})

    def get_delete_url(self):
        return reverse('services:serviceorder_delete', kwargs={'pk': str(self.id)})

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_name(self):
        return u"%s - %s - %s" % (self.service_type.name, self.client.name,
                                  self.price)