from django.urls import path
from .views import passagem

urlpatterns = [
    path('', passagem.index , name='index'),
]