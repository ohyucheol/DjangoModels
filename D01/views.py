import boto3
from urllib import parse
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import ComicBook
from .forms import ComicBookModelForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/D01/about.html"

class ListComicBookView(ListView):
    model = ComicBook
    paginate_by = 4
    context_object_name = 'ComicBook'
    template_name = 'DjangoApps/templates/D01/list-comicbook.html'

    def get_queryset(self):

        # 기본 queryset을 가져온다.
        queryset = super().get_queryset()

        # tag가 설정되어 있는 경우 해당 tag를 포함하는 ComicBook queryset을 가져온다.
        if 'tag' in self.request.GET:
            queryset = ComicBook.objects.all().filter(tag__contains=self.request.GET['tag'])

        # 가져온 queryset의 모든 ComicBook object에 대하여 공백으로 구분된 tag 값을 list로 변경한다.
        for q in queryset:
            q.tag = q.tag.split()
        return queryset

class CreateComicBookView(CreateView):
    model = ComicBook
    form_class = ComicBookModelForm
    template_name = 'DjangoApps/templates/D01/create-comicbook.html'
    success_url = '/D01/list/'

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

        if data['cover_file'] != None:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(settings.BUCKET)
            uploaded_cover = bucket.put_object(Body=data['cover_file'], Key=settings.PREFIX_D01 + '/' + data['cover_file'].name)

            encoded_key = parse.quote(uploaded_cover.key)

            self.object.cover = settings.S3_HOST + '/' + settings.BUCKET + '/' + encoded_key

        return super().form_valid(form)

class UpdateComicBookView(UpdateView):
    model = ComicBook
    form_class = ComicBookModelForm
    template_name = 'DjangoApps/templates/D01/update-comicbook.html'
    success_url = '/D01/list'

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

        if data['cover_file'] != None:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(settings.BUCKET)
            uploaded_cover = bucket.put_object(Body=data['cover_file'], Key=settings.PREFIX_D01 + '/' + data['cover_file'].name)

            encoded_key = parse.quote(uploaded_cover.key)
            
            self.object.cover = settings.S3_HOST + '/' + settings.BUCKET + '/' + encoded_key

        return super().form_valid(form)

class DeleteComicBookView(DeleteView):
    model = ComicBook
    template_name = 'DjangoApps/templates/D01/delete-comicbook.html'
    success_url = '/D01/list/'

    # def get_queryset(self):
    #     queryset = super(FormatListView, self).get_queryset().values()
    #     for f in queryset:
    #         books = Book.objects.filter(id=f['book_id'])
    #         f['books'] = books
    #     return queryset