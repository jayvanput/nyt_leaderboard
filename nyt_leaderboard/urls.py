"""nyt_leaderboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from leaderboard import views
from django.urls import include

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("<int:year>/<int:month>/<int:day>", views.PastPage.as_view(), name="past"),
    path("accounts/", include('authentication.urls')),
    path("date_picker", views.date_picker, name="date_picker"),
    path('admin/', admin.site.urls),
]
