from django.shortcuts import render, redirect
from django.db import connection

def submit_idea_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO your_app_idea (title, description) VALUES (%s, %s)", [title, description])
        return redirect('ideas_list')
    return render(request, 'submit_idea.html')

def ideas_list_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM your_app_idea")
        ideas = cursor.fetchall()
    return render(request, 'ideas_list.html', {'ideas': ideas})
