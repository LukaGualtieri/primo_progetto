from django.urls import path
from .views import home, listaArticoli

app_name = 'news'
urlpatterns = [
    path('', home, name="home"),
    path('lista_articoli/<int:pk>', listaArticoli, name="lista_articoli_giornalista"),
]
