from django.urls import path
from .views import About, ArticleListView, ArticleUpdateView


app_name = 'F01'

urlpatterns = [
    path('', About.as_view(), name='about'),

    path('article/', ArticleListView.as_view(), name='article-list'),
    # path('meetingroom/create/', MeetingRoomCreateView.as_view(), name='meetingroom-create'),
    # path('meetingroom/<int:pk>/', MeetingRoomDetailView.as_view(), name='meetingroom-detail'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('meetingroom/<int:pk>/delete/', MeetingRoomDeleteView.as_view(), name='meetingroom-delete'),

    # path('equipment/', EquipmentListView.as_view(), name='equipment-list'),
    # path('equipment/create/', EquipmentCreateView.as_view(), name='equipment-create'),
    # path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    # path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name='equipment-update'),
    # path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment-delete'),
]