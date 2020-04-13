from django.urls import path
from .views import passagem

urlpatterns = [
    path('', passagem.index , name='index'),
    path('minha_consulta', passagem.revisao_consulta, name='minha_consulta'),
]