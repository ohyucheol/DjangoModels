from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Writer
from .forms import WriterModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/C01/about.html"

class WriterListView(ListView):
    model = Writer
    paginate_by = 12
    context_object_name = 'writer'
    template_name = 'DjangoApps/templates/C01/writer-list.html'

class WriterDetailView(DetailView):
    model = Writer
    context_object_name = 'writer'
    template_name = 'DjangoApps/templates/C01/writer-detail.html'

class WriterCreateView(CreateView):
    model = Writer
    form_class = WriterModelForm
    template_name = 'DjangoApps/templates/C01/writer-form.html'
    success_url = '/C01/writer/'

class WriterUpdateView(UpdateView):
    model = Writer
    form_class = WriterModelForm
    template_name = 'DjangoApps/templates/C01/writer-form.html'
    success_url = '/C01/writer/'

class WriterDeleteView(DeleteView):
    model = Writer
    template_name = 'DjangoApps/templates/C01/writer-delete.html'
    success_url = '/C01/writer/'