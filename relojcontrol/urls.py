from django.urls import URLPattern, path
from . import views
from django.contrib.auth.views import (LoginView, logout_then_login)

urlpatterns = [
    path('ingreso', views.ingreso, name= 'ingreso'),
    path('home',views.home, name='home'),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout', logout_then_login, name='logout'),
    path('registro/', views.registro, name='registro'),
   
]
