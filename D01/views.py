from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Book, Format, DecimalClassification
from .forms import BookModelForm, FormatModelForm, DecimalClassificationModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/D01/about.html"

class BookListView(ListView):
    model = Book
    paginate_by = 12
    context_object_name = 'books'
    template_name = 'DjangoApps/templates/D01/booklist.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'DjangoApps/templates/D01/bookdetail.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookModelForm
    template_name = 'DjangoApps/templates/D01/bookcreate.html'
    success_url = '/D01/book/'

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookModelForm
    template_name = 'DjangoApps/templates/D01/bookupdate.html'
    success_url = '/D01/book/'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'DjangoApps/templates/D01/bookdelete.html'
    success_url = '/D01/book/'
    
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

class FormatDetailView(DetailView):
    model = Format
    context_object_name = 'format'
    template_name = 'DjangoApps/templates/D01/formatdetail.html'

class FormatCreateView(CreateView):
    model = Format
    form_class = FormatModelForm
    template_name = 'DjangoApps/templates/D01/formatcreate.html'
    success_url = '/D01/format/'

class FormatUpdateView(UpdateView):
    model = Format
    form_class = FormatModelForm
    template_name = 'DjangoApps/templates/D01/formatupdate.html'
    success_url = '/D01/format/'

class FormatDeleteView(DeleteView):
    model = Format
    template_name = 'DjangoApps/templates/D01/formatdelete.html'
    success_url = '/D01/format/'

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

class DecimalClassificationDetailView(DetailView):
    model = DecimalClassification
    context_object_name = 'decimalclassification'
    template_name = 'DjangoApps/templates/D01/decimalclassificationdetail.html'

class DecimalClassificationCreateView(CreateView):
    model = DecimalClassification
    form_class = DecimalClassificationModelForm
    template_name = 'DjangoApps/templates/D01/decimalclassificationcreate.html'
    success_url = '/D01/DecimalClassification/'

class DecimalClassificationUpdateView(UpdateView):
    model = DecimalClassification
    form_class = DecimalClassificationModelForm
    template_name = 'DjangoApps/templates/D01/decimalclassificationupdate.html'
    success_url = '/D01/decimalclassification/'

class DecimalClassificationDeleteView(DeleteView):
    model = DecimalClassification
    template_name = 'DjangoApps/templates/D01/decimalclassificationdelete.html'
    success_url = '/D01/decimalclassification/'