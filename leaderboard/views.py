from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from leaderboard.forms import EntryForm
from leaderboard.models import Entry
import datetime
# Create your views here.

class LeaderboardPage(View):
    form_class = EntryForm
    context = {}
    today = datetime.date.today()

    def get(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def get_zipped_entries_and_medals(self, page_date) -> zip:
        entries = self.get_todays_entries(page_date)
        medals = self.get_medals(entries)
        return zip(medals, entries)

    def get_dates(self,page_date) -> dict:
        yesterday = page_date - datetime.timedelta(days=1)
        tomorrow = page_date + datetime.timedelta(days=1)

        dates = {"page_date": page_date.strftime("%A, %B %d %Y")}
        dates["yesterday"] = yesterday.strftime("%Y/%m/%d")
        dates["tomorrow"] = tomorrow.strftime("%Y/%m/%d")
        dates["page_date_str"] = page_date.strftime("%Y-%m-%d")

        return dates

    def get_medals(self, entries):
        length_of_entries = len(entries)
        if length_of_entries <=3:
            medals = ["🥇","🥈","🥉"][0:length_of_entries]
        else:
            medals = ["🥇","🥈","🥉"] + [x for x in range(4,length_of_entries)]
        return medals

    
    def get_todays_entries(self,page_date):
        entries = Entry.objects.filter(created__year=page_date.year,created__month=page_date.month,created__day=page_date.day).order_by("hours","minutes","seconds","username")
        return entries

class HomePage(LeaderboardPage):
    form_class = EntryForm
    context = {}
    today = datetime.date.today()

    def get(self, request) -> HttpResponse:
        entry = self.form_class()

        self.context["form"] = entry
        self.context["entries"] = self.get_zipped_entries_and_medals(self.today)
        self.context["dates"] = self.get_dates(self.today)
        return render(request, "home.html",context=self.context)

    def post(self, request) -> HttpResponse:
        entry = self.form_class(request.POST)
        if entry.is_valid():
            entry.save()
            return redirect("/")

        self.context["form"] = entry
        self.context["entries"] = self.get_zipped_entries_and_medals(self.today)
        self.context["dates"] = self.get_dates(self.today)

        return render(request, "home.html",context=self.context)

    def get_dates(self,page_date) -> dict:
        yesterday = page_date - datetime.timedelta(days=1)

        dates = {"page_date": page_date.strftime("%A, %B %d %Y")}
        dates["yesterday"] = yesterday.strftime("%Y/%m/%d")
        dates["tomorrow"] = ""
        dates["page_date_str"] = page_date.strftime("%Y-%m-%d")

        return dates

class PastPage(LeaderboardPage):
    form_class = EntryForm
    context = {}
    today = datetime.date.today()

    def get(self, request, **kwargs):
        page_date = datetime.date(kwargs.get('year'), kwargs.get('month'), kwargs.get('day'))

        if page_date == self.today:
            return redirect("/")

        entry = self.form_class()

        self.context["form"] = entry
        self.context["entries"] = self.get_zipped_entries_and_medals(page_date)
        self.context["dates"] = self.get_dates(page_date)

        return render(request, "past.html",context=self.context)