from django.urls import path
from .views import HomePageView, FlightRegistrationView, FlightListView, FlightStatisticsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('flight_registration/', FlightRegistrationView.as_view(), name='flight_registration'),
    path('flight_list/', FlightListView.as_view(), name='flight_list'),
    path('flight_statistics/', FlightStatisticsView.as_view(), name='flight_statistics'),
    ]