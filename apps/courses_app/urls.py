from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^confirmdelete/(?P<id>\d+)$', views.confirmdelete),
    url(r'^delete$', views.delete),
]
