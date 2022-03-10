from django.forms import ModelForm, NumberInput, TextInput, BaseInlineFormSet
from leaderboard.models import Entry
from django import forms


class EntryForm(ModelForm):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control"}), initial="")
    hours = forms.IntegerField(
        widget=NumberInput(attrs={"class": "form-control time_input"}), initial=0, min_value=0, max_value=99)
    minutes = forms.IntegerField(
        widget=NumberInput(attrs={"class": "form-control time_input"}), initial=0, min_value=0, max_value=59)
    seconds = forms.IntegerField(
        widget=NumberInput(attrs={"class": "form-control time_input"}), initial=0, min_value=0, max_value=59)

    class Meta:
        model = Entry
        fields = ["username", "hours", "minutes", "seconds"]

    def clean(self):
        hours = self.cleaned_data.get("hours")
        minutes = self.cleaned_data.get("minutes")
        seconds = self.cleaned_data.get("seconds")
        if hours + minutes + seconds <= 0:
            raise forms.ValidationError("Invalid time")
