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
    objects = bucket.objects.all()

    if request.method == 'POST':
        keys = request.POST.getlist('keys[]')
        for k in keys:
            response = bucket.delete_objects(Delete={'Objects':[ {'Key': k} ]})
            
        objects = bucket.objects.all()
        return render(request, 'DjangoApps/templates/J01/list.html', {'objects':objects})
    else:
        return render(request, 'DjangoApps/templates/J01/list.html', {'objects':objects})

def upload(request):
    if request.method == 'POST':
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('testbucket.djangoapps')

        bucket.put_object(Body=request.FILES['file'], Key=request.FILES['file'].name)

        # pass
        return redirect('/J01/list')
        # return render(request, 'DjangoApps/templates/J01/upload.html', {'request':request})

    else:
        return render(request, 'DjangoApps/templates/J01/upload.html')