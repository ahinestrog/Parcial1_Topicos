from django.shortcuts import render
from django.views.generic import TemplateView
from flights.forms import FlightForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

# Formulario de registro de vuelo
class FlightRegistrationView(TemplateView):
    template_name = 'flight_registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flight_form'] = FlightForm()
        return context