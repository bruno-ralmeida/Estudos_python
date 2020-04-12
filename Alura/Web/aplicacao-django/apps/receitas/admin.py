from django.contrib import admin
from .models import Receita

# Register your models here.
class Listando_receitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicado') #Campos Filtrados
    list_display_links = ('id', 'nome_receita') #Links para edição
    search_fields = ('nome_receita',) #Busca por nome
    list_filter = ('categoria','publicado',) #Filtro lateral
    list_per_page = 10  #Definindo limite por pagina
    list_editable = ('publicado',)
admin.site.register(Receita, Listando_receitas)
