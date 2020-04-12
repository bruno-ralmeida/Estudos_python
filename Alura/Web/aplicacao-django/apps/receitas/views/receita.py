from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from receitas.models import Receita
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Função render, devemos passar o request como parametro.
def index(request):
    #Ordenando a lista de receitas na oredem reversa do campo data
    receitas = Receita.objects.order_by('-data_receita').filter(publicado=True) #Filtrando por campo
    paginator = Paginator(receitas,3)  
    page = request.GET.get('page')
    receitas_paginas = paginator.get_page(page)
    dados = {
        'receitas': receitas_paginas
    }
    return render(request,'receitas/index.html',dados)

def receita(request, receita_id):
    receita_exibir = get_object_or_404(Receita, pk=receita_id)
    receita = {
        'receita': receita_exibir
    }
    return render(request, 'receitas/receita.html', receita)

def cad_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita'] #Retornando arquivos
        

        user = get_object_or_404(User, pk=request.user.id) #Passando id do usuário logado

        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)

        receita.save()

        return redirect('dashboard')
    
    else:
        return render(request, 'receitas/cad_receita.html')

def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    dados = {
        'receita': receita
    }
    return render(request, 'receitas/editar_receita.html', dados)

def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r_atu = Receita.objects.get(pk=receita_id) #r_atu recebe o objeto de receita com id existente
        r_atu.nome_receita = request.POST['nome_receita'] #cada atributo do model vai receber as informações do formulário
        r_atu.ingredientes = request.POST['ingredientes']
        r_atu.modo_preparo = request.POST['modo_preparo']
        r_atu.tempo_preparo = request.POST['tempo_preparo']
        r_atu.rendimento = request.POST['rendimento']
        r_atu.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:   
            r_atu.foto_receita = request.FILES['foto_receita']

        r_atu.save() #Em django para atualizar os dados utilizamos o método save()
    return redirect('dashboard')
    
def exclui_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)   
    receita.delete()
    return redirect('dashboard')

    