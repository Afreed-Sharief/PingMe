from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from Pingme.models import FollowUser, MyPost, MyProfile, PostComment, PostLike
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView
from django.http.response import HttpResponseRedirect

# Create your views here.

class HomeView(TemplateView):
    template_name = "Pingme/home.html"

class AboutView(TemplateView):
    template_name = "Pingme/about.html"

class ContactView(TemplateView):
    template_name = "Pingme/contact.html"