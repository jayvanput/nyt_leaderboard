from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from leaderboard.forms import EntryForm
from leaderboard.models import Entry
from datetime import date
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
    entries = Entry.objects.all().order_by("hours","minutes","seconds","username")
    return render(request, "home.html", context={"entries": entries, "form": entry})

def past_leaderboards(request, year, month, day):
    dates = {"year": year, "month" :month, "day": day}
    entries = Entry.objects.filter(created__year=year,created__month=month,created__day=day)
    entry = EntryForm()
    return render(request, "past.html", context={"entries": entries, "form": entry,"dates":dates})