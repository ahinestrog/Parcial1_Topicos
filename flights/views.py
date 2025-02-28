from django.shortcuts import render
from django.views.generic import TemplateView
from flights.forms import FlightForm
from flights.models import Flight

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
    
# Listar vuelos

class FlightListView(TemplateView):
    template_name = 'flight_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = Flight.objects.all()
        return context

# Estadisticas de vuelos
class FlightStatisticsView(TemplateView):
    template_name = 'flight_statistics.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = Flight.objects.all()
        return context