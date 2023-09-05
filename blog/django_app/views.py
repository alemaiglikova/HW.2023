from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django_app.forms import PostForm, UserProfileForm
from django_app.models import UserProfile
from django.core.mail import send_mail
from django.contrib.auth import login


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Отправка письма
            subject = 'Добро пожаловать на наш сайт'
            message = 'Спасибо за регистрацию!'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('all_posts')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('all_posts')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'all_posts.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        if 'edit' in request.POST:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', post_id=post.id)
        elif 'delete' in request.POST:
            post.delete()
            return redirect('all_posts')
    else:
        form = PostForm(instance=post)

    return render(request, 'post_detail.html', {'post': post, 'form': form})


@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {'form': form})



