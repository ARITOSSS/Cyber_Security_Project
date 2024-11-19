from django.shortcuts import render
from django.http import HttpResponse

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