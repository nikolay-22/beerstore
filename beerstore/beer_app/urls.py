from django.urls import path

from beerstore.beer_app.views import BeerListView, BeerDetailsView

urlpatterns = [
    path('', BeerListView.as_view(), name='beer_list'),
    path('<int:pk>', BeerDetailsView.as_view(), name='beer_details'),
]