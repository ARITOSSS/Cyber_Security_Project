from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('file_upload_flaw/', views.file_upload_flaw, name='file_upload_flaw'),
    path('file_upload_fix/', views.file_upload_fix, name='file_upload_fix'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
