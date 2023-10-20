from django.contrib.auth.decorators import login_required

from django_app.models import Person, Article, Author, PublicModel, UserProfile
from django.shortcuts import render
from django_app.models import RestrictedModel
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django_app.models import Person
from django.shortcuts import render


def my_view(request):
    try:

        with transaction.atomic():

            new_people = [
                Person(name='Jane Doe', age=25),
                Person(name='Bob Smith', age=35),
                Person(name='Alice Johnson', age=40)
            ]
            Person.objects.bulk_create(new_people)


    except Exception as e:

        print(f"Error: {e}")


    return render(request, 'template.html')


person1 = Person.objects.create(name='John Doe', age=30)


all_persons = Person.objects.all()


young_people = Person.objects.filter(age__lt=25)


not_john = Person.objects.exclude(name='John Doe')

person_by_id = Person.objects.get(id=1)


sorted_people = Person.objects.order_by('age')


unique_names = Person.objects.values('name').distinct()


num_people = Person.objects.count()


first_person = Person.objects.first()
last_person = Person.objects.last()


john_exists = Person.objects.filter(name='John Doe').exists()


Person.objects.filter(name='John Doe').update(age=31)


Person.objects.filter(name='John Doe').delete()

new_people = [
    Person(name='Jane Doe', age=25),
    Person(name='Bob Smith', age=35),
    Person(name='Alice Johnson', age=40)
]
Person.objects.bulk_create(new_people)

author = Author.objects.select_related('book').get(id=1)
books = author.book.all()

authors = Author.objects.prefetch_related('book_set').all()
articles = Article.objects.select_related('tags').all()

articles = Article.objects.prefetch_related('tags').all()

person = Person.objects.select_related('profile').get(id=1)
profile = person.profile

people = Person.objects.prefetch_related('profile').all()



def public_data(request):
    public_data = PublicModel.objects.all()
    return render(request, 'public_data.html', {'public_data': public_data})

@login_required
def authenticated_no_restrictions_data(request):
    data = RestrictedModel.objects.all()
    return render(request, 'authenticated_no_restrictions_data.html', {'data': data})

@login_required
def own_data(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'own_data.html', {'user_profile': user_profile})

@login_required
def restricted_data(request):
    if request.user.is_staff:
        data = RestrictedModel.objects.all()
    else:
        data = None
    return render(request, 'restricted_data.html', {'data': data})

@login_required
def group_based_data(request):
    if request.user.groups.filter(name='Special Group').exists():
        data = RestrictedModel.objects.all()
    else:
        data = None
    return render(request, 'group_based_data.html', {'data': data})