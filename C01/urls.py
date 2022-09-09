from django.urls import path
from .views import About, NovelWriterListView, NovelWriterDetailView, NovelWriterCreateView, \
                    NovelWriterUpdateView, NovelWriterDeleteView


app_name = 'C01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('novel-writer/', NovelWriterListView.as_view(), name='writer-list'),
    path('novel-writer/create/', NovelWriterCreateView.as_view(), name='writer-create'),
    path('novel-writer/<int:pk>/', NovelWriterDetailView.as_view(), name='writer-detail'),
    path('novel-writer/<int:pk>/update/', NovelWriterUpdateView.as_view(), name='writer-update'),
    path('novel-writer/<int:pk>/delete/', NovelWriterDeleteView.as_view(), name='writer-delete'),
]