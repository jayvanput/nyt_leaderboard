from django.forms import ModelForm, NumberInput, TextInput
from django.contrib.auth.models import User
from django import forms


class UserForm(ModelForm):

    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control"}), initial="")
    password = forms.CharField(
        widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password"]

    