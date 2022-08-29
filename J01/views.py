from django.shortcuts import render, redirect
import boto3
# Create your views here.

def about(request):
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('testbucket.djangoapps')
    objects = bucket.objects.all()
    # buckets = s3.buckets.all()
    # services = s3.get_available_subresources()
    

    return render(request, 'DjangoApps/templates/J01/about.html', {'objects':objects})

def list(request):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('testbucket.djangoapps')

    if request.method == 'POST':
        keys = request.POST.getlist('keys[]')
        for k in keys:
            response = bucket.delete_objects(Delete={'Objects':[ {'Key': k} ]})

        objects = bucket.objects.all()
        return render(request, 'DjangoApps/templates/J01/list.html', {'objects':objects})
    else:
        objects = bucket.objects.all()
        return render(request, 'DjangoApps/templates/J01/list.html', {'objects':objects})

# def upload(request):
#     s3 = boto3.resource('s3')
#     bucket = s3.Bucket('testbucket.djangoapps')
    
#     if request.method == 'POST':
#         bucket.put_object(Body=request.FILES['file'], Key=request.FILES['file'].name)

#         return redirect('/J01/list')
#         # return render(request, 'DjangoApps/templates/J01/upload.html', {'request':request})

#     else:
#         return render(request, 'DjangoApps/templates/J01/upload.html')

def upload(request):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('testbucket.djangoapps')
    
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for f in files:
            bucket.put_object(Body=f, Key=f.name)

        return redirect('/J01/list')
        # return render(request, 'DjangoApps/templates/J01/upload.html', {'request':request})

    else:
        return render(request, 'DjangoApps/templates/J01/upload.html')