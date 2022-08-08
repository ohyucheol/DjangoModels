from django.shortcuts import render
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
