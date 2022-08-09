from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book, Format, DecimalClassification
# Create your views here.

def index(request):
    books = Book.objects.all().values()

    #Book의 id를 기준으로 Format, DecimalClassification 등을 받는다
    for b in books:
        formats = Format.objects.filter(book_id=b['id'])
        b['formats'] = formats

        # categories = DecimalClassification.objects.filter(book=b['id'])
        # b['categories'] = categories

    return render(request, 'DjangoApps/templates/D01/index.html', {'books' : books})


class BookListView(ListView):

    model = Book
    paginate_by = 1
    context_object_name = 'books'
    template_name = 'DjangoApps/templates/D01/booklistview.html'

    def get_queryset(self):
        queryset = super(BookListView, self).get_queryset().values()

        for book in queryset:
            formats = Format.objects.filter(book_id=book['id'])
            book['formats'] = formats

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aa'] = 'aa'
        return context