from django.contrib import admin
from .models import Pessoa

class Lista_pessoa(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome',)
    list_per_page = 10
    

# Register your models here.
admin.site.register(Pessoa, Lista_pessoa)