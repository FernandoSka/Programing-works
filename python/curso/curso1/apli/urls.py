from django.conf.urls import url
from apli import views
from apli.views import fecha
urlpatterns = [
	url(r'^land/$', views.current_datetime),	
    url(r'^fecha/', fecha.as_view(), name="fecha"),
]
