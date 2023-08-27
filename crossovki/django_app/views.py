from django.shortcuts import render
from .forms import ContactForm, ProductForm
from .models import Product

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Здесь можно добавить логику отправки письма или сохранения данных в базе данных
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
