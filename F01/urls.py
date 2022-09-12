from django.urls import path
from .views import About, ListArticleView, DetailArticleView, \
                    CreateArticleView, UpdateArticleView, DeleteArticleView, \
                    modal_list_file, modal_upload_file


app_name = 'F01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('list/', ListArticleView.as_view(), name='list'),
    path('create/', CreateArticleView.as_view(), name='create'),
    path('<int:pk>/detail/', DetailArticleView.as_view(), name='detail'),
    path('<int:pk>/update/', UpdateArticleView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteArticleView.as_view(), name='delete'),

    path('modal-list-file/', modal_list_file, name='modal-list-file'),
    path('modal-upload-file/', modal_upload_file, name='modal-upload-file'),
]