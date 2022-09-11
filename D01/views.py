from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import ComicBook
from .forms import ComicBookModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/D01/about.html"

class ListComicBookView(ListView):
    model = ComicBook
    paginate_by = 12
    context_object_name = 'books'
    template_name = 'DjangoApps/templates/D01/list-comicbook.html'

class CreateComicBookView(CreateView):
    model = ComicBook
    form_class = ComicBookModelForm
    template_name = 'DjangoApps/templates/D01/create-comicbook.html'
    success_url = '/D01/list/'

class UpdateComicBookView(UpdateView):
    model = ComicBook
    form_class = ComicBookModelForm
    template_name = 'DjangoApps/templates/D01/update-comicbook.html'
    success_url = '/D01/list'

class DeleteComicBookView(DeleteView):
    model = ComicBook
    template_name = 'DjangoApps/templates/D01/delete-comicbook.html'
    success_url = '/D01/list/'

    # def get_queryset(self):
    #     queryset = super(FormatListView, self).get_queryset().values()
    #     for f in queryset:
    #         books = Book.objects.filter(id=f['book_id'])
    #         f['books'] = books
    #     return queryset