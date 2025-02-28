from django.urls import path
from .views import HomePageView, FlightRegistrationView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('flight_registration/', FlightRegistrationView.as_view(), name='flight_registration'),
    ]