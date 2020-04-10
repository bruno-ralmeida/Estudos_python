from django.shortcuts import render

#Função render, devemos passar o request como parametro.
def index(request):
    return render(request,'index.html')

def receita(request):
    return render(request, 'receita.html')