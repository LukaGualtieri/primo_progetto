import datetime
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

def queryBase(request):
    #1.Tutti gli articoli scritti da giornalisti di un certo cognome:
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Gualtieri')
    
    #2.Totale
    numero_totale_articoli = Articolo.objects.count()

    #3.Contare il numero di articoli scritti da un giornalista specifico:
    giornalista_1 = Giornalista.objects.get(id=5)
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_1).count()

    #4.Ordinare gli articoli per numero di visualizzazioni in ordine decrescente
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')
                              
    #5.Tutti gli articoli che non hanno visualizzazioni:
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    #6.Articolo più visualizzato
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()
    
    #7.Tutti i giornalisti nati dopo una certa data:
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990, 1, 1))
    
    #8.Tutti gli articoli pubblicati in una data specifica:
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2022, 11, 14))
    
    #9.Tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo  = Articolo.objects.filter(data__range=(datetime.date(1990, 1, 1), datetime.date(2023, 12, 31)))
    
    #10.Gli articoli scritti da giornalisti nati prima del 1980:
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980, 1, 1)) 
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)
    
    #11.Il giornalista più giovane:
    giornalista_giovane = Giornalista.objects.order_by('anno_di_nascita').first()
    
    #12.Il giornalista più anziano:
    giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()
    
    #13.Gli ultimi 5 articoli pubblicati:
    ultimi = Articolo.objects.order_by('-data')[:5]
    
    #14.Tutti gli articoli con un certo numero minimo di visualizzazioni: 
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)
    
    #15.Tutti gli articoli che contengono una certa parola nel titolo: 
    articoli_parola = Articolo.objects.filter(titolo__icontains='ferrari')

    #16.Articoli pubblicati in un certo mese di un anno specifico:
    #nota per poter modificare la data di un articolo togliere la proprietà auto_now=True al field data nel model 
    #poi dare i comandi makemigrations e migrate per applicare le modifiche al database
    articoli_mese_anno = Articolo.objects.filter(data__month=2, data__year=1999)

    #17.Giornalisti con almeno un articolo con più di 100 visualizzazioni
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()
    """
    spiegazione dettagliata:
    Giornalista.objects: Inizia dalla classe del modello Giornalista.
    .filter(articoli__visualizzazioni__gte-100): Utilizza il metodo filter() per filtrare i giornalisti 
    in base al campo visualizzazioni nel modello Articolo. La notazione articoli_visualizzazioni indica 
    che si sta seguendo la relazione inversa dalla classe Giornalista alla classe Articolo attraverso 
    il campo ForeignKey giornalista nel modello Articolo.
    .distinct(): E' un metodo assicura che i risultati siano distinti, eliminando eventuali duplicati.
    In questo caso, ciò è utile perché un giornalista potrebbe essere associato a più articoli che soddisfano
    il criterio, e vogliamo ottenere solo una volta ogni giornalista che ha scritto almeno un articolo popolare.
    """

    #UTILIZZO DI PIU' CONDIZIONI DI SELEZIONE
    data = datetime.date(2000, 1, 1)
    visualizzazioni = 150
    #Per mettere in AND le condizioni separarle con la virgola
    #18.Tutti gli articoli scritti da dopo il 1/1/2000 e visualizzazioni con valore uguale o maggiore di 150: 
    articoli_con_and = Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzazioni)
    
    #Per mettere in OR le condizioni utilizzare l'operatore Q
    from django.db.models import Q
    #19.Tutti gli articoli scritti da dopo il 1/1/2000 o visualizzazioni con valore uguale o maggiore di 150: 
    articoli_con_or = Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=data) | Q(visualizzazioni__lte=visualizzazioni))
    #Per il NOT (~) utilizzare l'operatore Q
    #20.Tutti gli articoli scritti da prima del 1/1/2000: 
    articoli_con_not = Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt=data))
    #oppure il metodo exclude
    #con exclude vengono esclusi gli articoli con data minore del 1/1/2000
    articoli_con_not = Articolo.objects.exclude(giornalista__anno_di_nascita__lt=data)

    #Creare il dizionario context
    context = {
        'articoli_cognome' : articoli_cognome,
        'numero_totale_articoli' : numero_totale_articoli,
        'giornalista_1' : giornalista_1,
        'numero_articoli_giornalista_1' : numero_articoli_giornalista_1,
        'articoli_ordinati' : articoli_ordinati,
        'articoli_senza_visualizzazioni' : articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato' : articolo_piu_visualizzato,
        'giornalisti_data' : giornalisti_data,
        'articoli_del_giorno' : articoli_del_giorno,
        'articoli_periodo' : articoli_periodo,
        'giornalisti_nati' : giornalisti_nati,
        'articoli_giornalisti' : articoli_giornalisti,
        'giornalista_giovane' : giornalista_giovane,
        'giornalista_anziano' : giornalista_anziano,
        'ultimi' : ultimi,
        'articoli_minime_visualizzazioni' : articoli_minime_visualizzazioni,
        'articoli_parola' : articoli_parola,
        'articoli_mese_anno' : articoli_mese_anno,
        'giornalisti_con_articoli_popolari' : giornalisti_con_articoli_popolari,
        'articoli_con_and' : articoli_con_and,
        'articoli_con_or' : articoli_con_or,
        'articoli_con_not' : articoli_con_not,
    }
    return render(request, 'query.html', context)