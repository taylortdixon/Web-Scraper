from django.db import models

# Create your models here.
class Site(models.Model):
	site_id = models.AutoField(primary_key=True)
	site_url = models.URLField()
	list_ascending = models.BooleanField()
	table_identifier_type = models.CharField(max_length=5)
	row_identifier_type = models.CharField(max_length=5)
	song_name_identifier_type = models.CharField(max_length=5)
	song_artist_identifier_type = models.CharField(max_length=5)
	song_date_identifier_type = models.CharField(max_length=5)
	song_time_identifier_type = models.CharField(max_length=5)

   	table_identifier = models.CharField(max_length=150)
	row_identifier = models.CharField(max_length=150)
	song_name_identifier = models.CharField(max_length=150)
	song_artist_identifier = models.CharField(max_length=150)
	song_date_identifier = models.CharField(max_length=150)
	song_time_identifier = models.CharField(max_length=150)

class Song(models.Model):
	site_id = models.IntegerField()
	song_name = models.CharField(max_length=150)
	song_artist = models.CharField(max_length=200)
	song_datetime = models.DateTimeField()
	