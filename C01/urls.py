from django.urls import path
from .views import About, ListNovelWriterView, DetailNovelWriterView, CreateNovelWriterView, \
                    UpdateNovelWriterView, DeleteNovelWriterView


app_name = 'C01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('list/', ListNovelWriterView.as_view(), name='list'),
    path('create/', CreateNovelWriterView.as_view(), name='create'),
    path('<int:pk>/', DetailNovelWriterView.as_view(), name='detail'),
    path('<int:pk>/update/', UpdateNovelWriterView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteNovelWriterView.as_view(), name='delete'),
]