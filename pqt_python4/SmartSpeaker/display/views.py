from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message

def display_messages(request):
    messages = Message.objects.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display:display_messages')

    return render(request, 'display/messages.html', {'messages': messages, 'form': form})

