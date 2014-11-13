# -*- coding: utf-8 -*-
from django import forms

from client.models import Client
from services.models import MealOrder, MealType, ServiceOrder, ServiceType

TIME_RANGE = []
for i in range(7,22):
    for j in ("00", "30"):
        TIME_RANGE.append(("%s:%s" % (i,j), "%s:%s" % (i,j)))


class CommonOrderForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super(CommonOrderForm, self).__init__(*args, **kwargs)
        self.fields['client'] = forms.ModelChoiceField(
            Client.objects.order_by('id'),
            empty_label=None,
            required=True,
            label=u"Klient"
        )
        if self.instance.id:  # Only EditView has instance with id
            self.initial['order_time'] =\
                self.instance.order_time.strftime("%H:%M") \
                if self.instance.order_time else '' 


class MealOrderForm(CommonOrderForm):
    class Meta:
        model = MealOrder
        fields = ['meal_type', 'start_time', 'stop_time', 'order_time',
                  'client', 'price', 'serving']
    
    def __init__(self, *args, **kwargs):
        super(MealOrderForm, self).__init__(*args, **kwargs)
        self.fields['meal_type'] = forms.ModelChoiceField(
            MealType.objects.order_by('id'),
            empty_label=None,
            required=True,
            label=u"Typ dania"
        )


class ServiceOrderForm(CommonOrderForm):
    class Meta:
        model = ServiceOrder
        fields = ['service_type', 'start_time', 'stop_time', 'order_time',
                  'client', 'price']
    
    def __init__(self, *args, **kwargs):
        super(ServiceOrderForm, self).__init__(*args, **kwargs)
        self.fields['service_type'] = forms.ModelChoiceField(
            ServiceType.objects.order_by('id'),
            empty_label=None,
            required=True,
            label=u"Typ usługi"
        )
        self.fields['order_time'].label = u"Godzina wykonania"
