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
        entries = Entry.objects.all()
        if entry.is_valid():
            return redirect("/")
    else:
        entry = EntryForm()
    return render(request, "home.html", context={"entries": entries, "form": entry})


def post_time(request):
    if request.method == "POST":
        entry = EntryForm(request.POST)
        entries = Entry.objects.all()
        if entry.is_valid():
            print("good_form")
            return redirect("/")
        else:
            return render(request, "home.html", context={"entries": entries, "form": entry})
    entry = EntryForm()
    return render(request, "home.html", context={"entries": entries, "form": entry})
