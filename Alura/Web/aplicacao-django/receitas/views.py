from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

#Função render, devemos passar o request como parametro.
def index(request):
    #Ordenando a lista de receitas na oredem reversa do campo data
    receitas = Receita.objects.order_by('-data_receita').filter(publicado=True) #Filtrando por campo
    dados = {
        'receitas': receitas
    }
    return render(request,'index.html',dados)


def receita(request, receita_id):
    receita_exibir = get_object_or_404(Receita, pk=receita_id)
    receita = {
        'receita': receita_exibir
    }
    return render(request, 'receita.html', receita)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicado=True)
    if 'buscar' in request.GET:
        nome_busca = request.GET['buscar']
        if buscar:
         lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_busca) #__icontains é como o operador like
    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'buscar.html', dados)
