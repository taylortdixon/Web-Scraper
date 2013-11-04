from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User
    fields = ('url', 'username', 'email', 'groups')

class GroupViewSet(viewsets.ModelViewSet):
    model = Group
    fields = ('url', 'name')


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^data/', include('scanner.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # Examples:
    # url(r'^$', 'RadioScanner.views.home', name='home'),
    # url(r'^RadioScanner/', include('RadioScanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
