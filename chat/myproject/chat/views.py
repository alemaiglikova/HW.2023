from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Message
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def chat_room(request, username):
    user = get_object_or_404(User, username=username)
    messages = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(sender=user, receiver=request.user)
    messages = messages.order_by('timestamp')

    context = {
        'user': user,
        'messages': messages
    }

    return render(request, 'chat/chat_room.html', context)

@login_required
def send_message(request, username):
    if request.method == 'POST':
        content = request.POST.get('content')
        receiver = get_object_or_404(User, username=username)

        if content and receiver:
            message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def some_view_that_generates_notification(request):
    messages.success(request, 'Notification message text')
    return render(request, 'template.html')