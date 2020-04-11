from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

#Função render, devemos passar o request como parametro.
def index(request):
    receitas = Receita.objects.all()
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