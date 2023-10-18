from django_app.models import Person

from django.db import transaction
from myapp.models import Person
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


