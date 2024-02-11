from django.urls import path
from .views import indexNews, home, articoloDetailView, giornalistaDetailView, listaArticoli, queryBase, giornalista_api, giornalisti_list_api, articoli_list_api, articolo_api

app_name = 'news'
urlpatterns = [
    path('', indexNews, name='indexNews'),
    path('homeview/', home, name="homeview"),
    path('articoli/<int:pk>', articoloDetailView, name="articolo_detail"),
    path('giornalisti/<int:pk>', giornalistaDetailView, name="giornalista_detail"),
    path('lista_articoli/<int:pk>', listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/', listaArticoli, name="lista_articoli"),
    path('query_base/', queryBase, name="query_base"),
]
