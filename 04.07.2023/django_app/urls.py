import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django_app import models

def home(request):
    return render(request, 'home.html')