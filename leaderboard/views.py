from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from leaderboard.forms import EntryForm
from leaderboard.models import Entry

# Create your views here.


def home_page(request):
    entries = Entry.objects.all()
    if request.method == "POST":
        entry = EntryForm(request.POST)
        if entry.is_valid():
            entry.save()
            return redirect("/")
    else:
        entry = EntryForm()
    entries = Entry.objects.all()
    return render(request, "home.html", context={"entries": entries, "form": entry})
