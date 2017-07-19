from django.shortcuts import render
from urart.models import Artwork

def home(request):
	return render(request, 'home.html')

def upload(request):
	if request.method == 'POST':
		artwork = Artwork()
