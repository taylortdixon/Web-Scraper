from scanner.models import Song
from django.http import HttpResponse
from scanner.serializers import SongSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def index(request):
	all_songs = Song.objects.all()[:100]
	serializer = SongSerializer(all_songs)
	content = JSONRenderer().render(serializer.data)
	return HttpResponse(content)
