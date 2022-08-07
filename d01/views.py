from django.shortcuts import render
from .models import Book, BookMeta, Format, Category
# Create your views here.

def index(request):
    # books = Book.objects.all()
    # formats = Format.objects.all()

    # bookq = Book.objects.select_related('book')
    books = Book.objects.all().values()

    for b in books:
        formats = Format.objects.filter(book=b['id'])
        # for f in formats:
        #     b['format'] = f
        b['format'] = formats

    return render(request, 'DjangoApps/templates/D01/index.html', {'books' : books})
