from django.shortcuts import render
import boto3
# Create your views here.

def about(request):
	# Let's use Amazon S3
	s3 = boto3.resource('s3')
	buckets = s3.buckets.all()
	services = s3.get_available_services()
	

	return render(request, 'DjangoApps/templates/J01/about.html', {'buckets' : buckets})