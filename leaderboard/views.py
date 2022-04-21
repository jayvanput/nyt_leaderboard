from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from leaderboard.forms import EntryForm
from leaderboard.models import Entry
import datetime
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
    page_date = datetime.date(year, month, day)
    today = datetime.date.today()
    if page_date == today:
        return redirect("/")
    entries = Entry.objects.filter(created__year=page_date.year,created__month=page_date.month,created__day=page_date.day)
    return render(request, "past.html", context={"entries": entries, "dates":page_date})