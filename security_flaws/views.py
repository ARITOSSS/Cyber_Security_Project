from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import UserIDOR
# Create your views here.


def home(request):
    return render(request, 'security_flaws/home.html')

def xss_flaw(request):
    user_input = request.GET.get('user_input','')
    return render(request, 'security_flaws/xss_flaw.html' , {'user_input': user_input})

def xss_fix(request):
    user_input = request.GET.get('user_input','')
    return render(request, 'security_flaws/xss_fix.html' , {'user_input': user_input})

def csrf_flaw(request):
    if request.method == 'POST':
        user_data = request.POST.get('user_data', '')
        return HttpResponse(f"Data received : {user_data}")
    return render(request, 'security_flaws/csrf_flaw.html')

def csrf_fix(request):
    if request.method == 'POST':
        user_data = request.POST.get('user_data', '')
        return HttpResponse(f"Data received : {user_data}")
    return render(request, 'security_flaws/csrf_fix.html')

def sqli_flaw(request):
    user_data = None
    error = None
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')

        try:
            query = f"SELECT * FROM security_flaws_user WHERE username = '{username}' AND password = '{password}';"
            with connection.cursor() as cursor:
                cursor.execute(query)
                user_data = cursor.fetchall()  
        except Exception as e:
            error = str(e)

    return render(request, 'security_flaws/sqli_flaw.html', {'user_data': user_data, 'error': error})

def sqli_fix(request):
    user_data = None
    error = None
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')

        try:
            query = "SELECT * FROM security_flaws_user WHERE username = %s AND password = %s;"
            with connection.cursor() as cursor:
                cursor.execute(query, [username, password]) 
                user_data = cursor.fetchall()
        except Exception as e:
            error = str(e)

    return render(request, 'security_flaws/sqli_fix.html', {'user_data': user_data, 'error': error})

def user_idor_flaw(request,user_id):
    user = get_object_or_404(UserIDOR, id=user_id)
    return render(request, 'security_flaws/user_idor_flaw.html', {'user': user})

@login_required
def user_idor_fix(request,user_id):
    try :
        user = UserIDOR.objects.get(id=user_id)
        if user!=request.user:
            raise Http404("Accès refusé")
    except UserIDOR.DoesNotExist:
        raise Http404("Utilisateur introuvable")
    
    return render(request, 'security_flaws/user_idor_fix.html', {'user': user})