from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='username',
    )

    email = forms.EmailField(
        label = 'Email',
    )

    name = forms.CharField(
        label = 'Masukkan Nama:'
    )

    password1 = forms.CharField(
        label= 'Password',
        strip= False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'})
    )

    password1 = forms.CharField(
        label='Retype Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'password1', 'password2')


