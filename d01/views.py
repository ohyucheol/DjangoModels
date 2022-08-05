from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'DjangoApps/templates/D01/index.html')