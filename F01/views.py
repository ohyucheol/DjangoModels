from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Article
from .forms import ArticleModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/F01/about.html"

# Article
class ArticleListView(ListView):
    model = Article
    paginate_by = 12
    context_object_name = 'Article'
    template_name = 'DjangoApps/templates/F01/article-list.html'

# class ArticleDetailView(DetailView):
#     model = Article
#     context_object_name = 'Article'
#     template_name = 'DjangoApps/templates/F01/article-detail.html'

# class ArticleCreateView(CreateView):
#     model = Article
#     form_class = ArticleModelForm
#     template_name = 'DjangoApps/templates/F01/article-form.html'
#     success_url = '/F01/Article/'

# class ArticleUpdateView(UpdateView):
#     model = Article
#     form_class = ArticleModelForm
#     template_name = 'DjangoApps/templates/F01/article-form.html'
#     success_url = '/F01/Article/'

# class ArticleDeleteView(DeleteView):
#     model = Article
#     template_name = 'DjangoApps/templates/F01/article-delete.html'
#     success_url = '/F01/Article/'