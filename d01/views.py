from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.

def index(request):
    return render(request, 'DjangoApps/templates/D01/index.html')

class CreateView(CreateView):
    template_name = 'DjangoApps/templates/D01/index.html'