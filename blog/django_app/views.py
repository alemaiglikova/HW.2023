from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход пользователя после регистрации
            return redirect('all_posts')  # После успешной регистрации перенаправляем на страницу всех постов
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