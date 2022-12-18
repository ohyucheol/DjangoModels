import boto3
from urllib import parse
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import NovelWriter
from .forms import NovelWriterModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoModels/templates/C01/about.html"

class ListNovelWriterView(ListView):
    model = NovelWriter
    paginate_by = 12
    context_object_name = 'writer'
    template_name = 'DjangoModels/templates/C01/list-writer.html'

class DetailNovelWriterView(DetailView):
    model = NovelWriter
    context_object_name = 'writer'
    template_name = 'DjangoModels/templates/C01/detail-writer.html'

class CreateNovelWriterView(CreateView):
    model = NovelWriter
    form_class = NovelWriterModelForm
    template_name = 'DjangoModels/templates/C01/create-writer.html'
    success_url = '/C01/list/'

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

        # Model의 picture는 URLField이나 Form의 picture_file은 FileField로써 서로 맞지 않으므로
        # picture field를 제외한 나머지 값으로 object를 생성하고 데이터베이스에 저장한다.
        self.object = form.save()

        if data['picture_file'] != None:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(settings.BUCKET)
            uploaded_picture = bucket.put_object(Body=data['picture_file'], Key=settings.PREFIX_C01 + '/' + data['picture_file'].name)

            encoded_key = parse.quote(uploaded_picture.key)
            # 저장된 object의 picture field에 url을 입력한다.
            self.object.picture = settings.S3_HOST + '/' + settings.BUCKET + '/' + encoded_key

        return super().form_valid(form)

class UpdateNovelWriterView(UpdateView):
    model = NovelWriter
    form_class = NovelWriterModelForm
    template_name = 'DjangoModels/templates/C01/update-writer.html'
    success_url = '/C01/list/'

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
            uploaded_picture = bucket.put_object(Body=data['picture_file'], Key=settings.PREFIX_C01 + '/' + data['picture_file'].name)

            encoded_key = parse.quote(uploaded_picture.key)
            self.object.picture = settings.S3_HOST + '/' + settings.BUCKET + '/' + encoded_key

        return super().form_valid(form)

class DeleteNovelWriterView(DeleteView):
    model = NovelWriter
    template_name = 'DjangoModels/templates/C01/delete-writer.html'
    success_url = '/C01/list/'