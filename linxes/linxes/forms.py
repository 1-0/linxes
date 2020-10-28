from django import forms
from django.utils.translation import gettext as _
from . import models


class LinkForm(forms.ModelForm):

    class Meta:
        model = models.Link
        fields = ('long_link', )
        labels = {
            'long_link': _('Link'),
        }

