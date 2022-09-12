import boto3, datetime
from urllib import parse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import Article
from .forms import ArticleModelForm

# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/F01/about.html"

# Article
class ListArticleView(ListView):
    model = Article
    paginate_by = 12
    context_object_name = 'Article'
    template_name = 'DjangoApps/templates/F01/list-article.html'

class DetailArticleView(DetailView):
    model = Article
    context_object_name = 'Article'
    template_name = 'DjangoApps/templates/F01/detail-article.html'

class CreateArticleView(CreateView):
    model = Article
    form_class = ArticleModelForm
    template_name = 'DjangoApps/templates/F01/create-article.html'
    success_url = '/F01/list/'

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

        self.object.user_id = self.request.user.id
        self.object.published = datetime.datetime.now()
        self.object.modified = datetime.datetime.now()

        if data['thumbnail_file'] != None:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(settings.BUCKET)
            uploaded_thumbnail = bucket.put_object(Body=data['thumbnail_file'], Key=settings.PREFIX_F01 + '/' + data['thumbnail_file'].name)

            encoded_key = parse.quote(uploaded_thumbnail.key)

            self.object.thumbnail = settings.S3_HOST + '/' + settings.BUCKET + '/' + encoded_key

        return super().form_valid(form)

class UpdateArticleView(UpdateView):
    model = Article
    form_class = ArticleModelForm
    template_name = 'DjangoApps/templates/F01/update-article.html'
    success_url = '/F01/list/'

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

        if data['thumbnail_file'] != None:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(settings.BUCKET)
            uploaded_thumbnail = bucket.put_object(Body=data['thumbnail_file'], Key=settings.PREFIX_F01 + '/' + data['thumbnail_file'].name)

            encoded_key = parse.quote(uploaded_thumbnail.key)
            
            self.object.thumbnail = settings.S3_HOST + '/' + settings.BUCKET + '/' + encoded_key

        return super().form_valid(form)

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'DjangoApps/templates/F01/delete-article.html'
    success_url = '/F01/list/'

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
        # prefix를 추가할 필요가 있는 경우에는 objects = bucket.objects.filter(Prefix=settings.PREFIX_F01 + '/' + 'PREFIX2')
        objects = bucket.objects.filter(Prefix=settings.PREFIX_F01 + '/')
        return render(request, 'DjangoApps/templates/E01/modal-list-file.html', {'objects':objects})
    else:
        
        objects = bucket.objects.filter(Prefix=settings.PREFIX_F01 + '/')

        return render(request, 'DjangoApps/templates/E01/modal-list-file.html', {'objects':objects})

# AWS S3 파일 업로드를 위한 함수
@xframe_options_sameorigin
def modal_upload_file(request):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(settings.BUCKET)
    
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for f in files:
            bucket.put_object(Body=f, Key= settings.PREFIX_F01 + '/' + f.name)

        return redirect('/E01/modal-list-file/')

    else:
        return render(request, 'DjangoApps/templates/E01/modal-upload-file.html')