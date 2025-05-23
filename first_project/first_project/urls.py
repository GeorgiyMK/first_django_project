"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app.views import home_view, time_view, workdir_view, nasa_picture
from bus_stations.views import bus_stations
from calculator import views
from calculator.views import cook_calculator

urlpatterns = [
    path('', home_view, name='home'),
    # Раскомментируйте код, чтобы данные урлы 
    # обрабатывались Django
    path('nasa_picture/', nasa_picture, name='nasa_picture'),
    path('current_time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path('admin/', admin.site.urls),
    path('cook_calculator/', cook_calculator, name = 'cook_calculator'),
    path('dish/<str:dish_name>/', views.dish_detail, name='dish_detail'),
    path('bus_stations/', bus_stations, name='bus_stations'),
]
