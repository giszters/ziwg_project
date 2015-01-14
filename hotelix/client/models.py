# -*- coding: utf-8 -*-
from hashlib import md5

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

from structure.models import Room


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=u"Numer tel. musi być w formacie '+999999999'. Od 9 do 15. cyfr."
)

ORDER_CHOICES = (
    (0, u'wstępna'),
    (1, u'potwierdzona'),
    (2, u'zameldowany'),
    (3, u'zamknięty')
)

ORDER_COLORS = {
    0: '#C0C0C0',
    1: '#F400F4',
    2: '#2BAB0E',
    3: '#BD9700'
}


class Client(models.Model):
    created = models.DateTimeField(u"Utworzono", auto_now_add=True)
    name = models.CharField(u"Imię i nazwisko", max_length=100)
    # Pykniemy sobie regexp'a na numer telefonu?
    # http://stackoverflow.com/a/19131360
    # https://docs.djangoproject.com/en/dev/ref/validators/#regexvalidator
    telephone = models.CharField(u"nr tel.", max_length=20,
                                 validators=[phone_regex], blank=True)
    address = models.TextField(u"Adres", blank=True)
    description = models.TextField(u"Opis", blank=True)

    class Meta:
        verbose_name = u"Pacjent"
        verbose_name_plural = u"Pacjenci"

    def __unicode__(self):
        return u"%s) %s" % (self.id, self.name)

    def get_absolute_url(self):
        return reverse('client:client_edit', kwargs={'pk': str(self.id)})


class Order(models.Model):
    rooms = models.ManyToManyField(Room, null=False, verbose_name=u"Pokoje")
    number_of_people = models.IntegerField(u"Liczba gości", null=False)
    number_of_disabled = models.IntegerField(u"Liczba niepełnosprawnych",
                                             null=False, default=0)
    arrival_time = models.DateTimeField(u"Data przyjazdu", null=False)
    departure_time = models.DateTimeField(u"Data wyjazdu", null=False)
    # http://stackoverflow.com/a/2569044 Float vs Decimal Field
    price_per_night = models.DecimalField(u"Cena za noc", max_digits=10,
                                          decimal_places=2, null=False)
    client = models.ForeignKey(Client, null=False, verbose_name=u"Klient")
    description = models.TextField(u"Opis", null=True, blank=True)
    status = models.IntegerField(u"Status", null=False, choices=ORDER_CHOICES,
                                 default=0)

    class Meta:
        verbose_name = u"Zamówienie"
        verbose_name_plural = u"Zamówienia"

    def __unicode__(self):
        return u"zamówienie %s), klient: %s" % (self.id, self.client.name)

    def get_color(self):
        return ORDER_COLORS[self.status]

    def get_absolute_url(self):
        return reverse('client:order_edit', kwargs={'pk': str(self.id)})

