from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('xss_flaw/', views.xss_flaw, name='xss_flaw'),
    path('xss-fix/', views.xss_fix, name='xss_fix'),
    path('csrf_flaw/', views.csrf_flaw, name='csrf_flaw'),
    path('csrf_fix/', views.csrf_fix, name='csrf_fix'),
    path('sqli_flaw/', views.sqli_flaw, name='sqli_flaw'),
    path('sqli_fix/', views.sqli_fix, name='sqli_fix'),
    path('user/<int:user_id>/', views.user_idor_flaw, name='user_idor_flaw'),
    path('user/secure/<int:user_id>/', views.user_idor_fix, name='user_idor_fix'),

]
