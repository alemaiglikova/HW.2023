from django.shortcuts import render
import re
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import sqlite3

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        email = request.POST.get('email')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise Exception(f"Ошибка ввода почты {email}")

        username = request.POST.get('username')
        complaint = request.POST.get('complaint')

        with sqlite3.connect('database/db.db') as connection:
            cursor = connection.cursor()

            query = """
                INSERT INTO users (username, email, complaint) VALUES (?, ?, ?)
            """

            args = (username, email, complaint)

            cursor.execute(query, args)
            connection.commit()

        return HttpResponse("Метод в процессе реализации")
    else:
        return HttpResponse("Метод не реализован")
