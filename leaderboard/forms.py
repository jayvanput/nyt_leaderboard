from django.forms import ModelForm, TextInput
from leaderboard.models import Entry
from django import forms


class EntryForm(ModelForm):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control"}))
    hours = forms.CharField(
        widget=TextInput(attrs={"class": "form-control"}))
    minutes = forms.CharField(
        widget=TextInput(attrs={"class": "form-control"}))
    seconds = forms.CharField(
        widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Entry
        fields = ["username", "hours", "minutes", "seconds"]
