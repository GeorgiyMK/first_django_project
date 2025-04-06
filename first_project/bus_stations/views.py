import csv
import os

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    csv_path = os.path.join(settings.BASE_DIR, 'data-398-2018-08-30.csv')
    with open(csv_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        template_name = 'bus_stations/bus_stations.html'

        stations = list(reader)
        paginator = Paginator(stations, 15)
        page = paginator.get_page(page_number)
        pages = {
            'Главная страница': reverse('home'),
            'Показать текущее время': reverse('time'),
            'Картинка от NASA': reverse('nasa_picture'),
            'Показать содержимое рабочей директории': reverse('workdir'),
        }
        context = {
            'page': page,
            'pages' : pages
        }
        return render(request, template_name, context)

