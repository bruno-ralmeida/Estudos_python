from django.shortcuts import render
from receitas.models import Receita
from django.contrib import messages

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicado=True)
    if 'buscar' in request.GET:
        nome_busca = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_busca) #__icontains é como o operador like
    
    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'receitas/buscar.html', dados)
