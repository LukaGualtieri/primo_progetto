from django.shortcuts import render
import random

# Create your views here.
def indexx(request):
    return render(request, "indexx.html")

def maxmin(request):
    var1=random.randint(1, 10)
    var2=random.randint(1, 10)
    context={
        'var1' : var1,
        'var2' : var2,
        'var3' : var1+var2,
    }
    return render(request, "maxmin.html", context)

def media(request):
    lista = []
    for i in range(30):
        x=random.randint(1,10)
        lista.append(x)

    media=sum(lista)/30
    
    context={
        'lista' : lista,
        'media' : media,
    }
    return render(request, "media.html", context)

def voti(request):
    context={
        'voti' : {'studente 1':8, 'studente 2':7, 'studente 3':5, 'studente 4':8, 'studente 5':10 }, 
    }
    return render(request, "voti.html", context)

