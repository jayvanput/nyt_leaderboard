from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from authentication.forms import UserForm

# Create your views here.

class Auth(View):
    form_class = UserForm
    context = {}

    def get(self, request):
        user = self.form_class()

        self.context["form"] = user

        return render(request, "authentication/auth.html", context=self.context)
    
    def post(self, request):
        
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(f"you're a user {request.user}")
            return redirect("/")
        else:
            logout(request)
            return HttpResponse(f"You're not a user {request.user}!")