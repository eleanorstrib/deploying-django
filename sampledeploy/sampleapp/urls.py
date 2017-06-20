from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
]
