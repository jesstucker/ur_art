from rest_framework import serializers
from urart.models import Artwork

class ArtworkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artwork
		fields = ('id', 'title', 'url', 'artist')

