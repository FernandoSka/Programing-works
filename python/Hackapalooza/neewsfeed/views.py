from django.views.generic import (
    TemplateView,
    DetailView,
    ListView
)
from .models import New


class NewsFeed(TemplateView):
    model = New
    template_name = 'newsfeed.html'

    def get_context_data(self, **kwargs):
        context = super(NewsFeed, self).get_context_data(**kwargs)
        context['recently'] = New.objects.order_by('-created')
        context['rated'] = New.objects.order_by('-rating')
        return context
