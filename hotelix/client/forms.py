# -*- coding: utf-8 -*-
import datetime
from django import forms

from client.models import Order

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
        cd = self.cleaned_data
        if 'arrival_time' in cd and\
            'departure_time' in cd and\
            cd['arrival_time'] >= cd['departure_time']:
            raise forms.ValidationError(u"data przybycia >= data wyjazdu")
