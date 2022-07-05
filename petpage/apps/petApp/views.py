from django.shortcuts import render

# Create your views here.
def myIndexView(request, *args, **kwargs):
    return render(request, 'index.html',{})

def buy(request, *args, **kwargs):
    return render(request, 'buy.html',{})

def clinic(request, *args, **kwargs):
    return render(request, 'clinic.html',{})

def contact(request, *args, **kwargs):
    return render(request, 'contact.html',{})

def pet(request, *args, **kwargs):
    return render(request, 'pet.html',{})

def service(request, *args, **kwargs):
    return render(request, 'service.html',{})