from django.urls import path
from . import views
from .views import About, ListComicBookView, CreateComicBookView, UpdateComicBookView, DeleteComicBookView

app_name = 'D01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('list/', ListComicBookView.as_view(), name='list'),
    path('create/', CreateComicBookView.as_view(), name='create'),
    path('<int:pk>/update/', UpdateComicBookView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteComicBookView.as_view(), name='delete'),

]