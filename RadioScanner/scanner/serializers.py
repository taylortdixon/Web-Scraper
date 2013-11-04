from django.forms import widgets
from rest_framework import serializers
from scanner.models import Song

class SongSerializer(serializers.Serializer):
	pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
	site_id = serializers.IntegerField()
	song_name = serializers.CharField(required=True,
                                  max_length=150)
	song_artist = serializers.CharField(required=True,
                                  max_length=200)
	song_datetime = serializers.DateTimeField()

	def restore_object(self, attrs, instance=None):
		# Update existing instance
		if instance:
			instance.site_id = attrs.get('site_id', instance.site_id)
			instance.song_name = attrs.get('song_name', instance.song_name)
			instance.song_artist = attrs.get('song_artist', instance.song_artist)
			instance.song_datetime = attrs.get('song_datetime', instance.song_datetime)

			return instance
		return Song(**attrs) 