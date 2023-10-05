from django.urls import path
from prima_app.views import homepage
from prima_app.views import welcome
from prima_app.views import lista
from prima_app.views import chiSiamo
from prima_app.views import variabili
from prima_app.views import index




app_name="prima_app"
urlpatterns=[
    path('homepage', homepage, name='homepage'),
    path('welcome', welcome, name='welcome'),
    path('lista', lista, name='lista'),
    path('chiSiamo', chiSiamo, name='chiSiamo'),
    path('variabili', variabili, name='variabili'),
    path('', index, name='index'),
]