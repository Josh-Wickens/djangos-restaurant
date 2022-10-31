from django import forms
from django.forms import widgets
from django.conf import settings
from .models import Reservation
import datetime
from datetime import date

# Sets choices by the hour between 18:00 and 24:00
HOUR_CHOICES = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(18, 24)]


class ReserveTableForm(forms.ModelForm):
    # Form to book a table

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    class Meta:
        model = Reservation
        exclude = ('user', 'status', 'table')
        fields = '__all__'
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'}),
            'check_in': forms.Select(choices=HOUR_CHOICES),
        }
