from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
            email = forms.EmailField()
            first_name = forms.CharField(label='First name', max_length=100)
            last_name = forms.CharField(label='Last name', max_length=100)
            class Meta:
               model = User
               fields = ["first_name", "last_name",'username', 'email','password1', 'password2'] 