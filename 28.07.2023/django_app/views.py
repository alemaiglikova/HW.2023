from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

books_data = [
    {'title': f'Book {i}', 'description': f'Description of Book {i}', 'author': f'Author {i}'}
    for i in range(1, 101)
]


def book_list(request):
    page_number = request.GET.get('page', 1)

    paginator = Paginator(books_data, 10)

    try:

        page_obj = paginator.page(page_number)
    except EmptyPage:

        page_obj = paginator.page(paginator.num_pages)

        books = cache.get('book_list')

        if not books:
            books = books_data

            cache.set('book_list', books, timeout=300)

    return render(request, 'books/book_list.html', {'page_obj': page_obj})
