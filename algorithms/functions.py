from django.http import HttpResponse
import datetime
from django.contrib.auth import logout

def logout_view(request):
    logout(request)    
    return redirect('home')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)