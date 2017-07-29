from django.conf.urls import url, include
from urart import views
from accounts import views as account_views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'artwork-list/', views.artwork_list, name='artwork_list'),

    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),

	#rest framework
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^urart/', include('urart.urls')),
]
