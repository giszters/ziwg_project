# -*- coding: utf-8 -*-

from django import forms

from structure.models import Floor, Chamber, Room


TRUE_FALSE_CHOICES = (
    (True, u"Tak"),
    (False, u"Nie"),
)


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


class RoomForm(forms.ModelForm):
    for_disabled = forms.ChoiceField(label=u"Dla niepełnosprawnych",
        choices=TRUE_FALSE_CHOICES, required=True
    )

    class Meta:
        model = Room
        fields = ['name', 'beds', 'for_disabled', 'floor']
        widgets = {
            'floor': forms.widgets.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        floor_id = kwargs.pop('floor_id')
        super(RoomForm, self).__init__(*args, **kwargs)
        self.initial['floor'] = floor_id
