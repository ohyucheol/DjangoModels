from django.urls import path
from . import views
from .views import About, BookListView, FormatListView, DecimalClassificationListView

app_name = 'D01'

urlpatterns = [
    path('', About.as_view(), name='about'),
    path('book/', BookListView.as_view(), name='booklist'),
    path('format/', FormatListView.as_view(), name='formatlist'),
    path('decimalclassification/', DecimalClassificationListView.as_view(), name='decimalclassificationlist'),
    
]