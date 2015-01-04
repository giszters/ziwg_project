# -*- coding: utf-8 -*-
import datetime
from django import forms

from client.models import Order, Client, phone_regex

BOOLEAN_CHOICES = (
   (True, u"Tak"),
   (False, u"Nie")
)

class OrderForm(forms.ModelForm):
    arrival_time = forms.DateTimeField(label=u"Data przyjazdu", required=True,
        widget=forms.widgets.DateTimeInput(
           format="%Y-%m-%d %H:%M", attrs={'class': 'date_picker'}
        )
    )
    departure_time = forms.DateTimeField(label=u"Data wyjazdu", required=True,
        widget=forms.widgets.DateTimeInput(
           format="%Y-%m-%d %H:%M", attrs={'class': 'date_picker'}
        )
    )
    number_of_people = forms.IntegerField(label=u"Liczba gości", required=True,
        min_value=0)
    number_of_disabled = forms.IntegerField(label=u"Niepełnosprawni", required=True,
        min_value=0)
    description = forms.CharField(label=u"Opis", required=False,
        widget=forms.widgets.Textarea(attrs={'rows': '2', 'cols': '70'}))
    price_per_night = forms.DecimalField(label=u"Cena za noc", required=True,
        max_digits=10, decimal_places=2, localize=True)

    class Meta:
        model = Order

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

    def clean_arrival_time(self):
        arr_time = self.cleaned_data['arrival_time']
        if (arr_time.hour, arr_time.minute) == (0, 0):
            return datetime.datetime.combine(arr_time.date(), datetime.time(14,00))
        return arr_time

    def clean_departure_time(self):
        dep_time = self.cleaned_data['departure_time']
        if (dep_time.hour, dep_time.minute) == (0, 0):
            return datetime.datetime.combine(dep_time.date(), datetime.time(10,00))
        return dep_time

    def clean(self):
        cd = super(OrderForm, self).clean()
        if 'arrival_time' in cd and\
            'departure_time' in cd and\
            cd['arrival_time'] >= cd['departure_time']:
            raise forms.ValidationError(u"data przybycia >= data wyjazdu")
        return cd


class OrderCreateForm(OrderForm):
    create_new_client = forms.BooleanField(label=u"Nowy klient",
       widget=forms.widgets.Select(choices=BOOLEAN_CHOICES), required=False)
    client = forms.ModelChoiceField(queryset=Client.objects.order_by('-id'),
        label=u"Klient", required=False)
    client_name = forms.CharField(label=u"Imię i nazwisko", required=False)
    client_tel = forms.CharField(label=u"Telefon", required=False,
                                 validators=[phone_regex])
    client_address = forms.CharField(label=u"Adres", required=False)

    def __init__(self, *args, **kwargs):
        arr_date = kwargs.pop('arr_date')
        room_id = kwargs.pop('room_id')
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.initial['number_of_disabled'] = 0
        if arr_date:
            self.initial['arrival_time'] =\
                datetime.datetime.combine(
                    datetime.datetime.strptime(arr_date, "%Y-%m-%d"),
                    datetime.time(14,0)
                )
        if room_id:
            self.initial['rooms'] = room_id

    def clean(self):
        cleaned_data = super(OrderCreateForm, self).clean()
        if cleaned_data['create_new_client']:
            cleaned_data.pop('client', None)  # remove errors from Order model
            if not self.cleaned_data.get('client_name', ''):
                raise forms.ValidationError(u"Nowy klient musi mieć imię i nazw.")
        elif not cleaned_data.get('client'):
            cleaned_data.pop('client', None)  # remove errors from Order model
            raise forms.ValidationError(u"Nie wybrano istniejącego klienta")

    def save(self, *args, **kwargs):
        order = super(OrderCreateForm, self).save(commit=False, *args, **kwargs)
        cd = self.cleaned_data
        if cd['create_new_client']:
            client = Client.objects.create(
                name=cd['client_name'],
                telephone=cd['client_tel'],
                address=cd['client_address']
            )
            order.client = client
        order.save()
        for room in cd['rooms']:
            order.rooms.add(room)
        return order


class ClientForm(forms.ModelForm):
    address = forms.CharField(label=u"Adres", required=False,
        widget=forms.widgets.Textarea(attrs={'rows': '2', 'cols': '70'}))
    description = forms.CharField(label=u"Opis", required=False,
        widget=forms.widgets.Textarea(attrs={'rows': '2', 'cols': '70'}))

    class Meta:
        model = Client
        fields = ('name', 'address', 'telephone', 'description')

