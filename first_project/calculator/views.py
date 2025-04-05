from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from first_project.settings import DATA


def cook_calculator(request):
    template_name = 'calculator/cook_book.html'
    cook_book = DATA
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Картинка от NASA': reverse('nasa_picture'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {
        'cook_book': cook_book,
        'pages': pages,
            }
    return render(request, template_name, context)

def dish_detail(request, dish_name):
    try:
        quantity = int(request.GET.get('quantity', 1))
    except ValueError:
        quantity = 1
    template_name = 'calculator/dish_detail.html'
    dish = DATA.get(dish_name)
    if not dish:
        return HttpResponseNotFound("Такого блюда не существует")
    multiplied_ingredients = {
        name: round(amount * quantity, 2) for name, amount in dish.items()
    }

    context = {
        'dish_name': dish_name,
        'ingredients': multiplied_ingredients,
        'quantity': quantity,
    }

    return render(request, template_name, context)
