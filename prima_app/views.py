from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def welcome(request):
    return render(request, "welcome.html")

def lista(request):
    return render(request, "lista.html")

def chiSiamo(request):
    return render(request, "chiSiamo.html")