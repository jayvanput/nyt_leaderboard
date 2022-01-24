from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return HttpResponse("<title>NYTimes Crossword Leaderboard</title><h1>Leaderboard</h1>")
