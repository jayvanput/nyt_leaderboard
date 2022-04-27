from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from leaderboard.forms import EntryForm
from leaderboard.models import Entry
import datetime
# Create your views here.


def home_page(request):
    today = datetime.date.today()
    entries = Entry.objects.all()
    if request.method == "POST":
        entry = EntryForm(request.POST)
        if entry.is_valid():
            entry.save()
            return redirect("/")
    else:
        entry = EntryForm()
    entries = Entry.objects.filter(created__year=today.year,created__month=today.month,created__day=today.day).order_by("hours","minutes","seconds","username")
    
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    dates = {"yesterday": yesterday.strftime("%Y/%m/%d")}
    dates["today_input"] = today.strftime("%Y-%m-%d")

    return render(request, "home.html", context={"entries": entries, "form": entry, "dates":dates})

def past_leaderboards(request, year, month, day):
    page_date = datetime.date(year, month, day)
    today = datetime.date.today()
    if page_date == today:
        return redirect("/")
    entries = Entry.objects.filter(created__year=page_date.year,created__month=page_date.month,created__day=page_date.day)

    yesterday = page_date - datetime.timedelta(days=1)
    tomorrow = page_date + datetime.timedelta(days=1)

    dates = {"today": page_date.strftime("%A, %B %d %Y")}
    dates["yesterday"] = yesterday.strftime("%Y/%m/%d")
    dates["tomorrow"] = tomorrow.strftime("%Y/%m/%d")
    dates["today_input"] = today.strftime("%Y-%m-%d")


    return render(request, "past.html", context={"entries": entries, "dates":dates})

def date_picker(request):
    print(request.POST.get("nav__date"))

    picked_date = datetime.datetime.strptime(request.POST.get("nav__date"), "%Y-%m-%d")

    return redirect(f"{picked_date.year}/{picked_date.month}/{picked_date.day}")