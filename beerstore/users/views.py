# from django.contrib.auth.views import LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from beerstore.users.forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'

# class LogoutPageView(LogoutView):
#     success_url = reverse_lazy('home_page')
#     template_name = 'registration/logged_out.html'
