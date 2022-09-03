from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User
from .forms import UserCreateForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/A01/about.html"

class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'DjangoApps/templates/A01/user-form.html'
    success_url = '/A01/about/'