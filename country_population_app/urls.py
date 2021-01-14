from django.urls import path

from country_population_app import views

urlpatterns = [
    path('', views.home, name='home'),
]
