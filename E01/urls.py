from django.urls import path
from .views import About, ListMeetingRoomView, CreateMeetingRoomView, DetailMeetingRoomView, \
                    UpdateMeetingRoomView, DeleteMeetingRoomView, modal_list_file, modal_upload_file

app_name = 'E01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('list/', ListMeetingRoomView.as_view(), name='list'),
    path('create/', CreateMeetingRoomView.as_view(), name='create'),
    path('<int:pk>/detail/', DetailMeetingRoomView.as_view(), name='detail'),
    path('<int:pk>/update/', UpdateMeetingRoomView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteMeetingRoomView.as_view(), name='delete'),

    path('modal-list-file/', modal_list_file, name='modal-list-file'),
    path('modal-upload-file/', modal_upload_file, name='modal-upload-file'),
]