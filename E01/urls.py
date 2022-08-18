from django.urls import path
from .views import About, MeetingRoomListView, MeetingRoomDetailView, MeetingRoomCreateView, \
                    MeetingRoomUpdateView, MeetingRoomDeleteView, \
                    EquipmentListView, EquipmentDetailView, EquipmentCreateView, \
                    EquipmentUpdateView, EquipmentDeleteView \


app_name = 'E01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('meetingroom/', MeetingRoomListView.as_view(), name='meetingroom-list'),
    path('meetingroom/create/', MeetingRoomCreateView.as_view(), name='meetingroom-create'),
    path('meetingroom/<int:pk>/', MeetingRoomDetailView.as_view(), name='meetingroom-detail'),
    path('meetingroom/<int:pk>/update/', MeetingRoomUpdateView.as_view(), name='meetingroom-update'),
    path('meetingroom/<int:pk>/delete/', MeetingRoomDeleteView.as_view(), name='meetingroom-delete'),

    path('equipment/', EquipmentListView.as_view(), name='equipment-list'),
    path('equipment/create/', EquipmentCreateView.as_view(), name='equipment-create'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name='equipment-update'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment-delete'),
]