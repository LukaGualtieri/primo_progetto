from django.urls import path
from seconda_app.views import *


app_name="seconda_app"
urlpatterns=[
    path('es_if', es_if, name='es_if'),
]