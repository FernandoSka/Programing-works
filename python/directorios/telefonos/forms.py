from django.forms import ModelForm
from telefonos.models import Telefono
from django.contrib.auth.models import User

# Create the form class.


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class TelephoneForm(ModelForm):
    class Meta:
        model = Telefono
        fields = ['tel']
