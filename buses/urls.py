from django.urls import path
from .views import home_page,chatt

urlpatterns =[
    path('',home_page,name='urlpatterns'),
    

]