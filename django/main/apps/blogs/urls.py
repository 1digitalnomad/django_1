from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^test/$', views.test),
    url(r'^display/$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<number>\d+)/$', views.show),
    url(r'^(?P<num>\d+)/edit/$', views.edit),
    url(r'^(?P<num>\d+)/delete/$', views.destroy)
]