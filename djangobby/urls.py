"""
URL configuration for djangobby project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

from buses.views import *
from accou.views import RegisterView,UserSignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('buses.urls')),
  
    path('route/',fillroute,name='fillroute'),
    path('get_routes/',get_routes,name='get_routes'),
    # path('update/<int:update_id>/',updatee,name='updatee')
    path('remove/<int:busid>/',remove,name='remove'),
    path('update/<int:busid>/',updatee,name='updatee'),
    path('adds/',addroutes,name='addroutes'),
    path('get_areas/',get_areas,name='get_areas'),
    path('areas_update/<int:areaid>/',areas_update,name='areas_update'),
    path('usercred/',usercred,name='usercred'),
    # path('plot_areas/',plot_areas,name='plot_areas'),
    path('display_chart/',display_chart,name='display_chart'),
    # path('home_page/',home_page,name='home_page'),
    path('home_areas/',home_areas,name='home_areas'),
    path('api/register/',RegisterView.as_view(),name='register'),
    path('register/',register_page,name='register_page'),
    path('api/deatails',UserSignupView.as_view(),name='eatails'),
    path('api_areas/',api_areas,name='api_areas'),
    path('chat/',chatt,name='chatt'),



]
