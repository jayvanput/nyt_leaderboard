from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from leaderboard.forms import EntryForm
from leaderboard.models import Entry
import datetime
# Create your views here.

class HomePage(View):
    form_class = EntryForm
    context = {}
    today = datetime.date.today()

    def get(self, request) -> HttpResponse:
        entry = self.form_class()

        self.context["form"] = entry
        self.context["entries"] = self.get_zipped_entries_and_medals()
        self.context["dates"] = self.get_dates(self.today)
        return render(request, "home.html",context=self.context)

    def post(self, request) -> HttpResponse:
        entry = self.form_class(request.POST)
        if entry.is_valid():
            entry.save()
            return redirect("/")

        self.context["form"] = entry
        self.context["entries"] = self.get_zipped_entries_and_medals()
        self.context["dates"] = self.get_dates(self.today)

        return render(request, "home.html",context=self.context)

    def get_zipped_entries_and_medals(self) -> zip:
        entries = self.get_todays_entries(self.today)
        medals = self.get_medals(entries)
        return zip(medals, entries)

    def get_dates(self,page_date) -> dict:
        dates = {"today_input": page_date.strftime("%Y/%m/%d")}

        yesterday = page_date - datetime.timedelta(days=1)
        dates["yesterday"] = yesterday.strftime("%Y/%m/%d")

        return dates

    def get_medals(self, entries):
        length_of_entries = len(entries)
        if length_of_entries <=3:
            medals = ["🥇","🥈","🥉"][0:length_of_entries]
        else:
            medals = ["🥇","🥈","🥉"] + [x for x in range(4,length_of_entries)]
        return medals

    def get_todays_entries(self,date):
        entries = Entry.objects.filter(created__year=date.year,created__month=date.month,created__day=date.day).order_by("hours","minutes","seconds","username")
        return entries

class PastPage(View):
    form_class = EntryForm
    context = {}
    today = datetime.date.today()
    def get(self, request, **kwargs):
        self.page_date = datetime.date(kwargs.get('year'), kwargs.get('month'), kwargs.get('day'))

        if self.page_date == self.today:
            return redirect("/")

        entry = self.form_class()

        self.context["form"] = entry
        self.context["entries"] = self.get_zipped_entries_and_medals()
        self.context["dates"] = self.get_dates(self.page_date)

        return render(request, "past.html",context=self.context)

    
    def get_zipped_entries_and_medals(self) -> zip:
        entries = self.get_todays_entries(self.page_date)
        medals = self.get_medals(entries)
        return zip(medals, entries)

    
    def get_dates(self,page_date) -> dict:

        yesterday = page_date - datetime.timedelta(days=1)
        tomorrow = page_date + datetime.timedelta(days=1)

        dates = {"today": page_date.strftime("%A, %B %d %Y")}
        dates["yesterday"] = yesterday.strftime("%Y/%m/%d")
        dates["tomorrow"] = tomorrow.strftime("%Y/%m/%d")
        dates["today_input"] = page_date.strftime("%Y-%m-%d")

        return dates

    def get_medals(self, entries):
        length_of_entries = len(entries)
        if length_of_entries <=3:
            medals = ["🥇","🥈","🥉"][0:length_of_entries]
        else:
            medals = ["🥇","🥈","🥉"] + [x for x in range(4,length_of_entries)]
        return medals

    def get_todays_entries(self,date):
        entries = Entry.objects.filter(created__year=date.year,created__month=date.month,created__day=date.day).order_by("hours","minutes","seconds","username")
        return entries

def past_leaderboards(request, year, month, day):
    page_date = datetime.date(year, month, day)
    today = datetime.date.today()
    if page_date == today:
        return redirect("/")
    entries = Entry.objects.filter(created__year=page_date.year,created__month=page_date.month,created__day=page_date.day)

    # Build medals
    length_of_entries = len(entries)
    if length_of_entries <=3:
        medals = ["🥇","🥈","🥉"][0:length_of_entries]
    else:
        medals = ["🥇","🥈","🥉"] + [x for x in range(4,length_of_entries)]
    entries_display = zip(medals, entries)

    yesterday = page_date - datetime.timedelta(days=1)
    tomorrow = page_date + datetime.timedelta(days=1)

    dates = {"today": page_date.strftime("%A, %B %d %Y")}
    dates["yesterday"] = yesterday.strftime("%Y/%m/%d")
    dates["tomorrow"] = tomorrow.strftime("%Y/%m/%d")
    dates["today_input"] = today.strftime("%Y-%m-%d")


    return render(request, "past.html", context={"entries": entries_display, "dates":dates})

def date_picker(request):
    print(request.POST.get("nav__date"))

    picked_date = datetime.datetime.strptime(request.POST.get("nav__date"), "%Y-%m-%d")

    return redirect(f"{picked_date.year}/{picked_date.month}/{picked_date.day}")

# def home_page(request):
#     today = datetime.date.today()
#     entries = Entry.objects.all()
#     if request.method == "POST":
#         entry = EntryForm(request.POST)
#         if entry.is_valid():
#             entry.save()
#             return redirect("/")
#     else:
#         entry = EntryForm()
#     entries = Entry.objects.filter(created__year=today.year,created__month=today.month,created__day=today.day).order_by("hours","minutes","seconds","username")

#     # Build medals
#     length_of_entries = len(entries)
#     if length_of_entries <=3:
#         medals = ["🥇","🥈","🥉"][0:length_of_entries]
#     else:
#         medals = ["🥇","🥈","🥉"] + [x for x in range(4,length_of_entries)]
#     entries_display = zip(medals, entries)
#     yesterday = today - datetime.timedelta(days=1)

#     dates = {"yesterday": yesterday.strftime("%Y/%m/%d")}
#     dates["today_input"] = today.strftime("%Y-%m-%d")

#     return render(request, "home.html", context={"entries": entries_display, "form": entry, "dates":dates})
