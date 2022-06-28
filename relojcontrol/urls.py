from django.urls import URLPattern, path, re_path
from . import views
from relojcontrol.views import getCalendar
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('ingreso', views.ingreso, name= 'ingreso'),
    path('home',views.home, name='home'),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout', logout_then_login, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('reporte', views.Reporte, name='reporte'),
    path('salida', views.Salida, name='salida'),
    path('feriados', views.Feriados, name='feriados'),
    
    
    path('', getCalendar.as_view(template_name='calendar.html'), name='calendar View'),
    
   
    
    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name="reset_password"),
    path('password_reset_sent', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'),name="password_reset_done"),
    re_path('reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirms.html'), name = "password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_do.html') , name = "password_reset_complete"),
   
]

