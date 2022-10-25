from django import forms
from django.forms import widgets
from django.conf import settings
from .models import Reservation
import datetime

HOUR_CHOICES = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(18, 24)]

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ('user', 'status')
        fields = '__all__'
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'}),
            'check_in': forms.Select(choices=HOUR_CHOICES),
            # 'check_out': datetime.timedelta(minutes=90)
            # 'check_in': forms.TimeInput(attrs={'type': 'time'})
        }