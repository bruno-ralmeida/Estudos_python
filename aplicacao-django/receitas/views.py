from django.shortcuts import render

#Função render, devemos passar o request como parametro.
def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Sopa de Legumes',
        3: 'Sorvete',
        4: 'Bolo de chocolate'
    }
    dados = {
        'nome_receitas': receitas
    }
    return render(request,'index.html',dados)

def receita(request):
    return render(request, 'receita.html')