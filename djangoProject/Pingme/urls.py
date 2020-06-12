from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Pingme import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('', RedirectView.as_view(url="home/")),


]
