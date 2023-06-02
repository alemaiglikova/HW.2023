import re

from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
import hashlib


def home(request):
    return render(request, "home.html")



