import datetime
import os
import requests
import json

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    # Убрал переход с домашней страницы на домашнюю страницу, вроде не очень логично
    pages = {

        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
        'Картинка от NASA': reverse('nasa_picture'),
        'Кулинарный калькулятор' : reverse('cook_calculator')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # добавил HTML шаблон,
    template_name = 'app/home.html'

    # Запрос текущего времени и запись его в переменную msg
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'

    pages = {
        'Главная страница': reverse('home'),
        'Показать содержимое рабочей директории': reverse('workdir'),
        'Картинка от NASA': reverse('nasa_picture')
    }

    # добавил msg в context для отображения времени

    context = {
        'pages': pages,
        'msg': msg
    }

    return render(request, template_name, context)
    # return HttpResponse(msg)


def workdir_view(request):
    # Алгоритм действий аналогичный функции time_view
    template_name = 'app/home.html'
    list_cd = os.listdir('.')
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Картинка от NASA' : reverse('nasa_picture')
    }
    context = {
        'pages': pages,
        'list_cd': list_cd
    }

    return render(request, template_name, context)

def nasa_picture(request):
    # добавил HTML шаблон,
    template_name = 'app/home.html'

    nasa_url = 'https://api.nasa.gov/planetary/apod'

    params = {
        'api_key': 'JWkXF2uZbFi39O8bMmbm8gzCIti4JlGrAUj2Ekkx',
        'date': datetime.datetime.now().date()

    }
    response = requests.get(nasa_url, params=params)
    image_url = response.json()['url']

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages,
        'image_url': image_url
    }

    return render(request, template_name, context)