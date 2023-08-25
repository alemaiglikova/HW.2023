from django.shortcuts import render
from .models import News, Category

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'news/category_list.html', {'categories': categories})

def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'news/news_detail.html', {'news': news})
