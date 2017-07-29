from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from urart import views

urlpatterns = [
	url(r'^api/$', views.ArtworkListApi.as_view()),
	url(r'^api/(?P<pk>[0-9]+)/$', views.ArtworkDetail.as_view()),
	]

urlpatterns = format_suffix_patterns(urlpatterns)