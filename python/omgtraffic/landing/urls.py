from django.conf.urls import url
from landing.views import Map

urlpatterns = [
    url(r'^Map/',
        Map.as_view(),
        name='Map'),
]
