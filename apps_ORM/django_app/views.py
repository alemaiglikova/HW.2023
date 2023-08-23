from django.shortcuts import render, redirect
from .models import UsefulIdea
from .forms import UsefulIdeaForm


def submit_idea(request):
    if request.method == 'POST':
        form = UsefulIdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ideas_list')
    else:
        form = UsefulIdeaForm()

    return render(request, 'submit_idea.html', {'form': form})


def ideas_list(request):
    ideas = UsefulIdea.objects.all()
    return render(request, 'ideas_list.html', {'ideas': ideas})
