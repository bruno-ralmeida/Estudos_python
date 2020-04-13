from django.shortcuts import render
from passagens.forms import PassagemForms

# Create your views here.
def index(request):
    form = PassagemForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST) #Recuperando todas informações do formulário
        contexto = {'form':form} #Inserindo no contexto para ser renderizado no HTML
    return render(request, 'minha_consulta.html', contexto)