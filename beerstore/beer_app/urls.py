from django.urls import path

from beerstore.beer_app.views import BeerListView, BeerDetailsView, SearchResultsListView, ProducersListView, \
    BeerAddView, BeerEditView, beer_delete, ReviewAddView

urlpatterns = [
    path('', BeerListView.as_view(), name='beer_list'),
    path('<int:pk>', BeerDetailsView.as_view(), name='beer_details'),
    path('add/', BeerAddView.as_view(), name='beer_add'),
    path('edit/<int:pk>', BeerEditView.as_view(), name='beer_edit'),
    path('delete/<int:pk>', beer_delete, name='beer_delete'),
    path('reviews/', ReviewAddView.as_view(), name='beer_review'),
    path('producer/', ProducersListView.as_view(), name='producers_list'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]