from django.conf import settings
settings.configure(
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'radio_scanner',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}
)
from scanner.models import *
from django.conf import settings
import urllib2
from BeautifulSoup import BeautifulSoup
from dateutil import parser, relativedelta
import re


def scan_beat():
	baseurl = 'http://www.thebeat.com/music/playlist'
	
	basesoup = BeautifulSoup(get_full_response(baseurl))
	
	tablesoup = basesoup.find('table')

	for a in tablesoup('tr'):
		if len(a('td')) > 0:
			song =  a('td')
			song_date = song[0].contents[0].strip()
			song_time = song[1].contents[0].strip()
			song_name = song[2].contents[0].strip()
			song_artist = song[3].contents[0].strip() 
			
			song_datetime = create_date_object(song_date, song_time)
			if not is_song_processed(song_datetime):
				Song.objects.create(	song_datetime=song_datetime, 
											song_name=song_name, song_artist=song_artist)
				

def create_date_object(song_date, song_time):
	song_date = re.sub('\s+', ' ', song_date)
	#previous_date = relativedelta.relativedelta(days= -1)
	return parser.parse(song_date + " " + song_time) - previous_date
	
def get_full_response(url):
	fp = urllib2.urlopen(url)

	response = ""
	while 1:
		data = fp.read()
		if not data:
			break
		response += data

	return response

def is_song_processed(song_datetime):
	return Song.objects.filter(song_datetime=song_datetime).count() > 0


scan_beat()