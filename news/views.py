from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista

# Create your views here.
"""  V1
def home(request):
    a = "" #creo articolo
    g = "" #creo giornalista
    for art in Articolo.objects.all(): #con questo ciclo per ogni articolo presente in Articolo mostra il titolo
        a += (art.titolo + "<br>")
    
    for gio in Giornalista.objects.all(): #con questo ciclo per ogni giornalista presente in Giornalista mostra il nome
        g += (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g

    return HttpResponse("<h1>" + response + "</h1>")
"""

""" V2 --> in V1 il testo veniva concatenato in una variabile grazie ai cicli; in V2 tramite il ciclo il testo viene aggiunto nel vettore per poi essere mostrato
def home(request):
    a = [] #creo un vettore per gli articoli
    g = [] #creo un vettore per i giornalisti
    for art in Articolo.objects.all(): #con questo ciclo per ogni articolo presente in Articolo aggiunge il titolo al vettore a
        a.append(art.titolo)

    for gio in Giornalista.objects.all(): #con questo ciclo per ogni giornalista presente in Giornalista aggiunge il nome al vettore g
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")
"""    

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage1.html", context)

def articoloDetailView(request, pk):
    #articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

def listaArticoli(request, pk=None):
    if(pk == None):
        articoli = Articolo.objects.all()
        giornalista = None
    else: 
        articoli = Articolo.objects.filter(giornalista_id=pk)
        try:
            giornalista = Giornalista.objects.get(id=pk)
        except:
            giornalista = None

    context = {
        'articoli' : articoli,
        'giornalista' : giornalista,
        'pk' : pk,
    }
    return render(request, 'lista_articoli.html', context)