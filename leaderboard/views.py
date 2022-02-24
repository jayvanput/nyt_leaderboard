from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from leaderboard.models import Entry
# Create your views here.


def home_page(request):
    entries = Entry.objects.all()
    return render(request, "home.html", context={"entries": entries})


def post_time(request):
    hours = int(request.POST["hours"])
    minutes = int(request.POST["minutes"])
    seconds = int(request.POST["seconds"])

    entry = Entry.objects.create(
        username=request.POST["username"],
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        solve_time=hours*3600 + minutes*60 + seconds
    )
    entry.save()
    return redirect("/")
