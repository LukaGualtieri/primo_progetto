from django.urls import path
from .views import *

app_name = 'voti'
urlpatterns = [
    path('', indexVoti, name='indexVoti'),
    path('materiee', view_a, name="view_a"),
    path('voti_assenze', view_b, name="view_b"),
    path('media_voti', view_c, name="view_c"),
    path('maxMin_voti', view_d, name="view_d"),
]
