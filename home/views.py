from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .models import dishes
from math import ceil

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def nonveg(request):
    return render(request, 'nonveg.html')
 
def veg(request):
    return render(request, 'veg.html')

def starters(request):
    prod = dishes.objects.filter(category="starters")
    params = {'dishes': prod,'cat':''}
    return render(request, 'last.html', params)

def desserts(request):
    return render(request, 'desserts.html')
def bevrages(request):
    prod = dishes.objects.filter(category="bevrages")
    params = {'dishes': prod, 'cat':''}
    return render(request, 'last.html', params)

def chinese(request):
    prod = dishes.objects.filter(category="chinese")
    params = {'dishes': prod, 'cat': ''}
    return render(request, 'last.html', params)

def chicken(request):
    prod = dishes.objects.filter(category="chicken")
    params = {'dishes': prod, 'cat': 'nonveg'}
    return render(request, 'last.html',params)

def mutton(request):
    prod = dishes.objects.filter(category="mutton")
    params = {'dishes': prod, 'cat': 'nonveg'}
    return render(request, 'last.html',params)

def beaf(request):
    prod = dishes.objects.filter(category="beaf")
    params = {'dishes': prod, 'cat': 'nonveg'}
    return render(request, 'last.html',params)

def paneer(request):
    prod = dishes.objects.filter(category="paneer")
    params = {'dishes': prod, 'cat': 'veg'}
    return render(request, 'last.html',params)

def veggies(request):
    prod = dishes.objects.filter(category="veggies")
    params = {'dishes': prod, 'cat': 'veg'}
    return render(request, 'last.html',params)

def others(request):
    prod = dishes.objects.filter(category="others")
    params = {'dishes': prod , 'cat': 'veg'}
    return render(request, 'last.html',params)
def icecream(request):
    prod = dishes.objects.filter(category="icecream")
    params = {'dishes': prod , 'cat': 'desserts'}
    return render(request, 'last.html',params)
def halwa(request):
    prod = dishes.objects.filter(category="halwa")
    params = {'dishes': prod , 'cat': 'desserts'}
    return render(request, 'last.html',params)
def special(request):
    prod = dishes.objects.filter(category="special")
    params = {'dishes': prod , 'cat': 'desserts'}
    return render(request, 'last.html',params)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 