from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import MeetingRoom, Equipment
from .forms import MeetingRoomModelForm, EquipmentModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/E01/about.html"

# MeetingRoom
class MeetingRoomListView(ListView):
    model = MeetingRoom
    paginate_by = 12
    context_object_name = 'meetingroom'
    template_name = 'DjangoApps/templates/E01/meetingroom-list.html'

class MeetingRoomDetailView(DetailView):
    model = MeetingRoom
    context_object_name = 'meetingroom'
    template_name = 'DjangoApps/templates/E01/meetingroom-detail.html'

class MeetingRoomCreateView(CreateView):
    model = MeetingRoom
    form_class = MeetingRoomModelForm
    template_name = 'DjangoApps/templates/E01/meetingroom-form.html'
    success_url = '/E01/meetingroom/'

class MeetingRoomUpdateView(UpdateView):
    model = MeetingRoom
    form_class = MeetingRoomModelForm
    template_name = 'DjangoApps/templates/E01/meetingroom-form.html'
    success_url = '/E01/meetingroom/'

class MeetingRoomDeleteView(DeleteView):
    model = MeetingRoom
    template_name = 'DjangoApps/templates/E01/meetingroom-delete.html'
    success_url = '/E01/meetingroom/'

#Equipment
class EquipmentListView(ListView):
    model = Equipment
    paginate_by = 12
    context_object_name = 'equipment'
    template_name = 'DjangoApps/templates/E01/equipment-list.html'

class EquipmentDetailView(DetailView):
    model = Equipment
    context_object_name = 'equipment'
    template_name = 'DjangoApps/templates/E01/equipment-detail.html'

class EquipmentCreateView(CreateView):
    model = Equipment
    form_class = EquipmentModelForm
    template_name = 'DjangoApps/templates/E01/equipment-form.html'
    success_url = '/E01/equipment/'

class EquipmentUpdateView(UpdateView):
    model = Equipment
    form_class = EquipmentModelForm
    template_name = 'DjangoApps/templates/E01/equipment-form.html'
    success_url = '/E01/equipment/'

class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'DjangoApps/templates/E01/equipment-delete.html'
    success_url = '/E01/equipment/'