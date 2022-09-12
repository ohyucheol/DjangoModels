import boto3
from urllib import parse
from django.conf import settings
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
    success_url = '/E01/list/'

    def form_invalid(self, form):
        for f in self.form_class.Meta.fields:
            if form.has_error(f):
                for err in form.errors[f]:
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        data = form.cleaned_data

        self.object = form.save()

        if data['picture_file'] != None:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(settings.BUCKET)
            uploaded_picture = bucket.put_object(Body=data['picture_file'], Key=settings.PREFIX_E01 + '/' + data['picture_file'].name)

            encoded_key = parse.quote(uploaded_picture.key)

            self.object.picture = settings.S3_HOST + '/' + settings.BUCKET + '/' + encoded_key

        return super().form_valid(form)

class UpdateMeetingRoomView(UpdateView):
    model = MeetingRoom
    form_class = MeetingRoomModelForm
    template_name = 'DjangoApps/templates/E01/update-meetingroom.html'
    success_url = '/E01/list/'

    def form_invalid(self, form):
        for f in self.form_class.Meta.fields:
            if form.has_error(f):
                for err in form.errors[f]:
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        data = form.cleaned_data

        if data['picture_file'] != None:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(settings.BUCKET)
            uploaded_picture = bucket.put_object(Body=data['picture_file'], Key=settings.PREFIX_E01 + '/' + data['picture_file'].name)

            encoded_key = parse.quote(uploaded_picture.key)
            
            self.object.picture = settings.S3_HOST + '/' + settings.BUCKET + '/' + encoded_key

        return super().form_valid(form)

class DeleteMeetingRoomView(DeleteView):
    model = MeetingRoom
    template_name = 'DjangoApps/templates/E01/delete-meetingroom.html'
    success_url = '/E01/list/'
