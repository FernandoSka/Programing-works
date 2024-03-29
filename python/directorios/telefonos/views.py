from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import TemplateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from .models import Telefono
from django.views.generic.base import RedirectView

# Create your views here.


def home(request):
    return render(request, 'home.html')


class LoginDir(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("telefonos:sesion")
    success_message = "Welcome back %(username)s!"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            print(True)
            return redirect(self.get_success_url())
        else:
            print(False)
            return super(LoginDir, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginDir, self).form_valid(form)


class Registro(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "registro.html"
    success_url = reverse_lazy("telefonos:login")
    success_message = "User was created successfully"


class Sesion(ListView):
    model = Telefono

    template_name = "sesion.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Sesion, self).dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Sesion, self).get_context_data(**kwargs)
        return context


class Logout(RedirectView):
    pattern_name = 'telefonos:index'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)
