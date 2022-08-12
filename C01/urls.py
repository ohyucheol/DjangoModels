from django.urls import path
from .views import About, WriterListView, WriterDetailView, WriterCreateView, \
                    WriterUpdateView, WriterDeleteView


app_name = 'C01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('writer/', WriterListView.as_view(), name='writer-list'),
    path('writer/create/', WriterCreateView.as_view(), name='writer-create'),
    path('writer/<int:pk>/', WriterDetailView.as_view(), name='writer-detail'),
    path('writer/<int:pk>/update/', WriterUpdateView.as_view(), name='writer-update'),
    path('writer/<int:pk>/delete/', WriterDeleteView.as_view(), name='writer-delete'),
]