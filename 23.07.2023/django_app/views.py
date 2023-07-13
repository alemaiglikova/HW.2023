from django import template
from django.shortcuts import render

def registration_view(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")




        return render(request, "registration_success.html")


    return render(request, "registration_form.html")


register = template.Library()

@register.simple_tag
def format_number(number):

    formatted_number = "{:,.2f}".format(number)
    return formatted_number





@register.filter
def capitalize_word(word):

    return word.capitalize()






@register.simple_tag
def custom_greeting(name):

    greeting = f"Привет, {name}!"
    return greeting
