from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Book, Format, DecimalClassification
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/D01/about.html"

class BookListView(ListView):
    model = Book
    paginate_by = 12
    context_object_name = 'books'
    template_name = 'DjangoApps/templates/D01/booklist.html'

class FormatListView(ListView):
    model = Format
    paginate_by = 12
    context_object_name = 'formats'
    template_name = 'DjangoApps/templates/D01/formatlist.html'

    # queryset 내의 추가적인 context_data를 위한 오버라이드
    def get_queryset(self):
        queryset = super(FormatListView, self).get_queryset().values()
        for f in queryset:
            books = Book.objects.filter(id=f['book_id'])
            f['books'] = books
        return queryset

class DecimalClassificationListView(ListView):
    model = DecimalClassification
    paginate_by = 12
    context_object_name = 'decimalclassification'
    template_name = 'DjangoApps/templates/D01/decimalclassificationlist.html'

    # queryset 내의 추가적인 context_data를 위한 오버라이드
    def get_queryset(self):
        queryset = super(DecimalClassificationListView, self).get_queryset().values()
        for dc in queryset:
            books = Book.objects.filter(id=dc['book_id'])
            dc['books'] = books
        return queryset