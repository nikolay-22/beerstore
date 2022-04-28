from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from beerstore.beer_app.forms import BeerAddForm, BeerEditForm, BeerDeleteForm, ReviewAddForm
from beerstore.beer_app.models import Beer, Producer, Review


class BeerListView(LoginRequiredMixin, ListView):
    model = Beer
    context_object_name = 'beer_list'
    template_name = 'beers/beer_list.html'
    login_url = 'login'
    ordering = ['brand']


class BeerDetailsView(LoginRequiredMixin, DetailView):
    model = Beer
    context_object_name = 'beer'
    template_name = 'beers/beer_details.html'
    login_url = 'login'


class BeerAddView(LoginRequiredMixin, CreateView):
    model = Beer
    template_name = 'beers/beer_add.html'
    form_class = BeerAddForm
    success_url = reverse_lazy('beer_list')


class BeerEditView(LoginRequiredMixin, UpdateView):
    model = Beer
    template_name = 'beers/beer_edit.html'
    form_class = BeerEditForm
    success_url = reverse_lazy('beer_list')


# class BeerDeleteView(LoginRequiredMixin, DeleteView):
#     model = Beer
#     template_name = 'beers/beer_delete.html'
#     form_class = BeerDeleteForm
#     success_url = reverse_lazy('beer_list')


def beer_delete(request, pk):
    beer = Beer.objects.get(pk=pk)
    if request.method == 'POST':
        beer.delete()
        return redirect('beer_list')
    else:
        form = BeerDeleteForm(initial=beer.__dict__)
        context = {
            'form': form,
            'beer': beer,
        }
        return render(request, 'beers/beer_delete.html', context)


class ProducersListView(ListView):
    model = Producer
    context_object_name = 'producer_list'
    template_name = 'beers/producer_list.html'
    ordering = ['name']


class SearchResultsListView(ListView):
    model = Beer
    context_object_name = 'beer_list'
    template_name = 'beers/beer_search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')

        return Beer.objects.filter(
            Q(brand__icontains=query) | Q(producer__name__icontains=query)
        )


class ReviewAddView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'beers/beer_review.html'
    form_class = ReviewAddForm
    success_url = reverse_lazy('beer_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
