from django.shortcuts import render, redirect
from .models import Service, TeamMember
from .forms import ContactForm

def home(request):
    services = Service.objects.all()
    team_members = TeamMember.objects.all()
    return render(request, 'home.html', {'services': services, 'team_members': team_members})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы, например, отправка письма
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
