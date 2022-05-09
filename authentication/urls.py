from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path("auth", views.Auth.as_view(), name="auth")
]
