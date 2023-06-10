from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from .models import USER_REG


class RegisterUserForms(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'from-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'from-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'from-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'from-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'from-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'from-input'}),

        }
class USERFORM(ModelForm):
    class Meta:
        model = USER_REG
        fields = ['NAME', 'YEAR', 'NUMBER', 'KURS', 'USER']
        widgets = {
            'KURS': TextInput(attrs={'readonly': "readonly", 'class':'nons'}),
            'USER': TextInput(attrs={'readonly': "readonly", 'class': 'nons'}),

        }