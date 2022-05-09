from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    print(request.user)
    return render(request, "authentication/index.html")

class Auth(View):
    
    def post(self, request):
        
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)
        logout(request)
        if user is not None:
            login(request,user)
            return HttpResponse(f"Welcome Back {request.user}!")

        else:
            return HttpResponse(f"You're not a user {request.user}!")