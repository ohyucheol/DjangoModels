from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'DjangoApps/templates/a00/signin.html')

def signup(request):
    return render(request, 'DjangoApps/templates/a00/signup.html')

def signin(request):
    return render(request, 'DjangoApps/templates/a00/signin.html')