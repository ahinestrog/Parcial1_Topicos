import django.forms as forms
from.models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'type', 'price']

        