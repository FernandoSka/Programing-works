from django.shortcuts import render
from django.http import HttpResponse
from apli.models import Usuario
import datetime
from django.views.generic import ListView, View, TemplateView

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
# Create your views here.
class fecha(TemplateView):
    template_name = "fecha.html"