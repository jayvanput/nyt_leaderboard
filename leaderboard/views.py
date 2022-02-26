from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from leaderboard.forms import EntryForm
from leaderboard.models import Entry
# Create your views here.


def home_page(request):
    form = EntryForm
    entries = Entry.objects.all()
    return render(request, "home.html", context={"entries": entries, "form": form})


def post_time(request):
    entry = Entry.objects.create(
        username=request.POST["username"],
        solve_time=int(request.POST["hours"])*3600 +
        int(request.POST["minutes"])*60 + int(request.POST["seconds"])
    )
    entry.save()
    return redirect("/")
