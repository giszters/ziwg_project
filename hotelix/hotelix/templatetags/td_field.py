# -*- coding: utf-8 -*-
from django import forms
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# very important - HTML must be unicode, not str
HTML = u"""<tr>
    <th>%(errors)s %(label)s</th>
    <td>%(field)s</td>
</tr>"""

@register.simple_tag
def td_field(field):
    # https://docs.djangoproject.com/en/1.7/howto/custom-template-tags/#simple-tags
    # http://stackoverflow.com/a/8163802
    return HTML % {
        'errors': field.errors,
        'label': field.label_tag(),
        'field': forms.forms.BoundField(field.form, field.field, field.name)
    }
    