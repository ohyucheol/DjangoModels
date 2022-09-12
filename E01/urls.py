from django.urls import path
from .views import About, ListMeetingRoomView, CreateMeetingRoomView, DetailMeetingRoomView, \
                    UpdateMeetingRoomView, DeleteMeetingRoomView

app_name = 'E01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('list/', ListMeetingRoomView.as_view(), name='list'),
    path('create/', CreateMeetingRoomView.as_view(), name='create'),
    path('<int:pk>/', DetailMeetingRoomView.as_view(), name='detail'),
    path('<int:pk>/update/', UpdateMeetingRoomView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteMeetingRoomView.as_view(), name='delete'),
]