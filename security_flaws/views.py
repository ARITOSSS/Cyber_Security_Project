from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
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
        return HttpResponse(f"Données reçues : {user_data}")
    return render(request, 'security_flaws/csrf_flaw.html')

def csrf_fix(request):
    if request.method == 'POST':
        user_data = request.POST.get('user_data', '')
        return HttpResponse(f"Données reçues : {user_data}")
    return render(request, 'security_flaws/csrf_fix.html')

def sqli_flaw(request):
    user_data = None
    error = None
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')

        try:
            # Requête SQL brute vulnérable
            query = f"SELECT * FROM security_flaws_user WHERE username = '{username}' AND password = '{password}';"
            with connection.cursor() as cursor:
                cursor.execute(query)
                user_data = cursor.fetchall()  # Retourne une liste de tuples
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
            # Requête sécurisée avec des paramètres
            query = "SELECT * FROM security_flaws_user WHERE username = %s AND password = %s;"
            with connection.cursor() as cursor:
                cursor.execute(query, [username, password])  # Paramètres sécurisés
                user_data = cursor.fetchall()
        except Exception as e:
            error = str(e)

    return render(request, 'security_flaws/sqli_fix.html', {'user_data': user_data, 'error': error})
