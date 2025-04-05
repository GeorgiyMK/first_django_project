import csv
import os

from django.conf import settings
from django.shortcuts import render

def bus_stations(request):
    csv_path = os.path.join(settings.BASE_DIR, 'data-398-2018-08-30.csv')
    with open(csv_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        template_name = 'bus_stations/bus_stations.html'
        
        return render(request, template_name, context)

