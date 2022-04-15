from django.shortcuts import render
from django.http import HttpResponse
import random

import passgen

# Create your views here.
def home(request):
    return render(request, 'passgen/home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*_?'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('length', 12))

    thepassword = ''
    for i in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'passgen/password.html', {'password':thepassword})

def info(request):
    return render(request, 'passgen/info.html')