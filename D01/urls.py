from django.urls import path
from . import views
from .views import About, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, \
                    FormatListView, FormatDetailView, FormatCreateView, FormatUpdateView, FormatDeleteView, \
                    DecimalClassificationListView, DecimalClassificationDetailView, \
                    DecimalClassificationCreateView, DecimalClassificationUpdateView, DecimalClassificationDeleteView

app_name = 'D01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('book/', BookListView.as_view(), name='booklist'),
    path('book/create/', BookCreateView.as_view(), name='bookcreate'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='bookdetail'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='bookupdate'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='bookdelete'),

    path('format/', FormatListView.as_view(), name='formatlist'),
    path('format/create/', FormatCreateView.as_view(), name='formatcreate'),
    path('format/<int:pk>/', FormatDetailView.as_view(), name='formatdetail'),
    path('format/<int:pk>/update/', FormatUpdateView.as_view(), name='formatupdate'),
    path('format/<int:pk>/delete/', FormatDeleteView.as_view(), name='formatdelete'),

    path('decimalclassification/', DecimalClassificationListView.as_view(), name='decimalclassificationlist'),
    path('decimalclassification/create/', DecimalClassificationCreateView.as_view(), name='decimalclassificationcreate'),
    path('decimalclassification/<int:pk>/', DecimalClassificationDetailView.as_view(), name='decimalclassificationdetail'),
    path('decimalclassification/<int:pk>/update/', DecimalClassificationUpdateView.as_view(), name='decimalclassificationupdate'),
    path('decimalclassification/<int:pk>/delete/', DecimalClassificationDeleteView.as_view(), name='decimalclassificationdelete'),
]