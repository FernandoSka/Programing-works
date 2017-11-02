from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(regex=r'^logout/$',
        view=views.logout_view,
        name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social'))
]
