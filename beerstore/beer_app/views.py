from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from beerstore.beer_app.models import Beer


class BeerListView(ListView):
    model = Beer
    context_object_name = 'beer_list'
    template_name = 'beers/beer_list.html'


class BeerDetailsView(DetailView):
    model = Beer
    context_object_name = 'beer'
    template_name = 'beers/beer_details.html'

