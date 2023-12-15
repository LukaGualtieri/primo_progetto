from django.shortcuts import render

# Create your views here.
def indexVoti(request):
    return render(request, "indexVoti.html")


def view_a(request):
    context={
        'materie' : ["Matematica","Italiano","Inglese","Storia","Geografia"],
    }
    return render(request, "materie.html", context)


def view_b(request):
    context={
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
                  'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
                  'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request, "voti_assenze.html", context)


def view_c(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
            'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
            'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

    medie = {}
    for studente, materie in voti.items():
        somma=0
        tot_materie=0
        for materia,voto,assenze in materie:
            somma+=voto
            tot_materie+=1
            media=somma/tot_materie
            medie[studente]=media

    context={
        'voti' : voti,
        'media' : media, 
        'medie' : medie,
    }
    return render(request, "media_voti.html", context)


def view_d(request):
    context={
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
                  'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
                  'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request, "maxMin_voti.html", context)
