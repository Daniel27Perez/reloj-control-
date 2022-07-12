"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

urlpatterns = [
    path('ingreso', views.ingreso, name= 'ingreso'),
    path('salida', views.Termino, name= 'salida'),
    path('home',views.home, name='home'),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout', logout_then_login, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('reporte', views.Reporte, name='reporte'),
    path('feriados', views.Feriados, name='feriados'),
    path('calendar', views.Calendario, name='calendar'),
    path('asistencia', views.Asistencia, name='asistencia'),
    




    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login.html', success_url=reverse_lazy('Coloca tu URL')), name = 'login'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_confirms.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_do', PasswordResetDoneView.as_view(template_name='registration/password_reset_do.html'), name = 'password_reset_do'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),
   
]
