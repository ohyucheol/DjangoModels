from django.shortcuts import render
import boto3
# Create your views here.

def about(request):
	# Let's use Amazon S3
	s3 = boto3.resource('s3')
	buckets = s3.buckets.all()

	return render(request, 'DjangoApps/templates/J01/about.html', {'buckets' : buckets})    