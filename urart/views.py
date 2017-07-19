from django.shortcuts import render, redirect
from urart.models import Artwork
import boto
from django.conf import settings
from django.contrib.auth.models import User

def home(request):
	return render(request, 'home.html')

def upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		artwork = Artwork.objects.create(artist=request.user)
		pic = request.FILES['myfile']
		
		conn = boto.connect_s3(aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
			aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, is_secure=False)
		bucket = conn.get_bucket('urart')
		key = bucket.new_key(str(artwork.id))
		key.set_contents_from_file(pic)

		artwork.url = key.generate_url(9999999)

		# artwork.artist = request.user
		# artwork.title = request.POST['title']
		artwork.save()

		return redirect('upload')
	else:
		return render(request, 'upload.html')