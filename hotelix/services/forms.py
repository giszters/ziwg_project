# -*- coding: utf-8 -*-
from django import forms

from client.models import Client
from services.models import MealOrder, MealType

TIME_RANGE = []
for i in range(10,19):
    for j in ("00", "30"):
        TIME_RANGE.append(("%s:%s" % (i,j), "%s:%s" % (i,j)))


class MealOrderForm(forms.ModelForm):
    start_time = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'date_picker'}),
        label=u"Czas rozpoczęcia", required=True)
    stop_time = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'date_picker'}),
        label=u"Czas zakończenia", required=True
    )
    order_time = forms.ChoiceField(
        label=u"Godzina podania",
        choices=TIME_RANGE,
        required=False
    )
    class Meta:
        model = MealOrder
        fields = ['meal_type', 'start_time', 'stop_time', 'order_time',
                  'client', 'price']
    def __init__(self, *args, **kwargs):
        super(MealOrderForm, self).__init__(*args, **kwargs)
        self.fields['meal_type'] = forms.ModelChoiceField(
            MealType.objects.order_by('id'),
            empty_label=None,
            required=True,
            label=u"Typ dania"
        )
        self.fields['client'] = forms.ModelChoiceField(
            Client.objects.order_by('id'),
            empty_label=None,
            required=True,
            label=u"Klient"
        )
        #import ipdb; ipdb.set_trace()
        self.initial['order_time'] = self.instance.order_time.strftime("%H:%M")
        