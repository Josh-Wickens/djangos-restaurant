from django import forms
from django.forms import widgets
from django.conf import settings
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ('user',)
        fields = '__all__'
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }