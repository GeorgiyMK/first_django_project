from django.shortcuts import render
from django.urls import reverse

from first_project.settings import DATA


def cook_calculator(request):
    # quantity = request.GET.get('quantity', 1)
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
