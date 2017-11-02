from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (
    TemplateView,
    FormView
)
from .forms import SignUpForm
from .models import Volunteer


def logout_view(request):
    """Logout the user."""
    logout(request)
    return redirect('/')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class SignUpView(FormView):
    """This view show our Sign Up Form."""

    template_name = 'signup.html'
    form_class = SignUpForm

    def form_valid(self, form):
        """If the form is valid we save the new user."""
        user = form.save()
        user.refresh_from_db()
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        fields = [
            form.cleaned_data.get('second_last_name'),
            form.cleaned_data.get('calle'),
            form.cleaned_data.get('colonia'),
            form.cleaned_data.get('municipio'),
            form.cleaned_data.get('estado'),
            form.cleaned_data.get('telefono'),
        ]
        volunteer = Volunteer.objects.create(user=user)
        volunteer.second_last_name = fields[0]
        volunteer.calle = fields[1]
        volunteer.colonia = fields[2]
        volunteer.municipio = fields[3]
        volunteer.estado = fields[4]
        volunteer.telefono = fields[5]
        volunteer.save()
        login(self.request, user)
        return redirect('cms:home')
