import boto3
from urllib import parse
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
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

# 이하는 tinyMCE에서의 AWS S3 파일 관리를 위한 함수

# AWS S3 파일 목록 전시, 삭제를 위한 함수
@xframe_options_sameorigin
def modal_list_file(request):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(settings.BUCKET)

    if request.method == 'POST':
        keys = request.POST.getlist('keys')
        for k in keys:
            response = bucket.delete_objects(Delete={'Objects':[ {'Key': k} ]})

        # 버킷 내 특정 폴더(prefix)에 해당하는 파일만을 가져온다.
        # 모든 파일을 가져올 필요가 있는 경우에는 objects = bucket.objects.all(),
        # prefix를 추가할 필요가 있는 경우에는 objects = bucket.objects.filter(Prefix=settings.PREFIX_E01 + '/' + 'PREFIX2')
        objects = bucket.objects.filter(Prefix=settings.PREFIX_E01 + '/')
        return render(request, 'DjangoApps/templates/E01/modal-list-file.html', {'objects':objects})
    else:
        
        objects = bucket.objects.filter(Prefix=settings.PREFIX_E01 + '/')

        return render(request, 'DjangoApps/templates/E01/modal-list-file.html', {'objects':objects})

# AWS S3 파일 업로드를 위한 함수
@xframe_options_sameorigin
def modal_upload_file(request):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(settings.BUCKET)
    
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for f in files:
            bucket.put_object(Body=f, Key= settings.PREFIX_E01 + '/' + f.name)

        return redirect('/E01/modal-list-file/')

    else:
        return render(request, 'DjangoApps/templates/E01/modal-upload-file.html')