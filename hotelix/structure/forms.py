# -*- coding: utf-8 -*-

from django import forms

from structure.models import Floor, Chamber


class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['number', 'house']
        widgets = {
            'house': forms.widgets.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        house_id = kwargs.pop('house_id')
        super(FloorForm, self).__init__(*args, **kwargs)
        self.initial['house'] = house_id


class ChamberForm(forms.ModelForm):
    class Meta:
        model = Chamber
        fields = ['description', 'house']
        widgets = {
            'house': forms.widgets.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        house_id = kwargs.pop('house_id')
        super(ChamberForm, self).__init__(*args, **kwargs)
        self.initial['house'] = house_id