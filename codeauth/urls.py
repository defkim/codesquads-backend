from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^djoser/', include('djoser.urls')),
	url(r'^djoser/', include('djoser.urls.authtoken')),
]