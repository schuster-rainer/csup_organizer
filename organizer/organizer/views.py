from django.shortcuts import  render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib import messages

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"
