from django.conf.urls import patterns, url

from scanner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)