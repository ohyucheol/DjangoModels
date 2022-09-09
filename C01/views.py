from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import NovelWriter
from .forms import NovelWriterModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/C01/about.html"

class NovelWriterListView(ListView):
    model = NovelWriter
    paginate_by = 12
    context_object_name = 'writer'
    template_name = 'DjangoApps/templates/C01/writer-list.html'

class NovelWriterDetailView(DetailView):
    model = NovelWriter
    context_object_name = 'writer'
    template_name = 'DjangoApps/templates/C01/writer-detail.html'

class NovelWriterCreateView(CreateView):
    model = NovelWriter
    form_class = NovelWriterModelForm
    template_name = 'DjangoApps/templates/C01/writer-form.html'
    success_url = '/C01/writer/'

class NovelWriterUpdateView(UpdateView):
    model = NovelWriter
    form_class = NovelWriterModelForm
    template_name = 'DjangoApps/templates/C01/writer-form.html'
    success_url = '/C01/writer/'

class NovelWriterDeleteView(DeleteView):
    model = NovelWriter
    template_name = 'DjangoApps/templates/C01/writer-delete.html'
    success_url = '/C01/writer/'