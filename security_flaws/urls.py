from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('xss_flaw/', views.xss_flaw, name='xss_flaw'),
    path('xss-fix/', views.xss_fix, name='xss_fix'),

]
