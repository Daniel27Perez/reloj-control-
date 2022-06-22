from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('ingreso', views.ingreso, name= 'ingreso'),
    path('home',views.home, name='home')
   
]
