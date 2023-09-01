from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'hsdfghjkliuy'})

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    password = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    
    length = request.GET.get('length')
    if request.GET.get('uppercase'):
        chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        chars.extend('0,1,2,3,4,5,6,7,8,9')
    if request.GET.get('special'):
        chars.extend('&#{[|-]}_^@)=$*!')
    for x in range(int(length)):
        password += random.choice(chars)
    

    return render(request, 'generator/password.html', {'password':password})
