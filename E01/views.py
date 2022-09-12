from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import MeetingRoom
from .forms import MeetingRoomModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/E01/about.html"

# MeetingRoom
class ListMeetingRoomView(ListView):
    model = MeetingRoom
    paginate_by = 12
    context_object_name = 'MeetingRoom'
    template_name = 'DjangoApps/templates/E01/list-meetingroom.html'

class DetailMeetingRoomView(DetailView):
    model = MeetingRoom
    context_object_name = 'MeetingRoom'
    template_name = 'DjangoApps/templates/E01/detail-meetingroom.html'

class CreateMeetingRoomView(CreateView):
    model = MeetingRoom
    form_class = MeetingRoomModelForm
    template_name = 'DjangoApps/templates/E01/create-meetingroom.html'
    success_url = '/E01/meetingroom/'

class UpdateMeetingRoomView(UpdateView):
    model = MeetingRoom
    form_class = MeetingRoomModelForm
    template_name = 'DjangoApps/templates/E01/update-meetingroom.html'
    success_url = '/E01/meetingroom/'

class DeleteMeetingRoomView(DeleteView):
    model = MeetingRoom
    template_name = 'DjangoApps/templates/E01/delete-meetingroom.html'
    success_url = '/E01/meetingroom/'