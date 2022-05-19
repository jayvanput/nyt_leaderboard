from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.Auth.as_view(), name='accounts'),
]
