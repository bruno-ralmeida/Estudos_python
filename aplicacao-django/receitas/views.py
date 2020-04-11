from django.shortcuts import render
from .models import Receita
#Função render, devemos passar o request como parametro.
def index(request):
    receitas = Receita.objects.all()
    dados = {
        'receitas': receitas
    }
    return render(request,'index.html',dados)

def receita(request):
    return render(request, 'receita.html')