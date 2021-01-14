from django.shortcuts import render

# Create your views here.
from country_population_app.models import Country


def home(request):
    countries = Country.objects.all()
    return render(request, 'home.html', {'countries': countries})