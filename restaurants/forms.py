from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VoteForm(forms.Form):
    restaurant_id = forms.IntegerField()


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
