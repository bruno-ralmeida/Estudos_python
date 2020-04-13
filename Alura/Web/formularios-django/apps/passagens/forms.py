from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
"""

É necessário instalar o tempus-dominus ( pip install django-tempus-dominus)

https://pypi.org/project/django-tempus-dominus/

Instalação
	• Do PyPI: pip install django-tempus-dominus
Em seguida, adicione tempus_dominusa INSTALLED_APPSem suas configurações do Django.
Configurações de uso e Django
As seguintes configurações estão disponíveis:
	• TEMPUS_DOMINUS_LOCALIZE(padrão :) False: se True, os widgets serão traduzidos para o idioma selecionado do navegador e usarão os formatos de data e hora localizados.
	• TEMPUS_DOMINUS_INCLUDE_ASSETS(padrão :) True: se Truecarrega Tempus Dominus e momentJS e CSS da CDN do Cloudflare, caso contrário, o carregamento de JS e CSS depende de você.
São fornecidos três widgets:
	• DatePicker
		○ O padrão é YYYY-MM-DD
		○ O padrão é LseTEMPUS_DOMINUS_LOCALIZETrue
	• DateTimePicker
		○ O padrão é YYYY-MM-DD HH:mm:ss
		○ O padrão é L LTSseTEMPUS_DOMINUS_LOCALIZETrue
	• TimePicker
		○ O padrão é HH:mm:ss
		○ O padrão é LTSseTEMPUS_DOMINUS_LOCALIZETrue


Após realizar as configurções é necessário realizar a importação do DatePicker no nosso forms.py

from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


Após realizar a importação é necessário incluir novas informações no nosso forms.py

from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
class PassagemForms(forms.Form):
    data_ida = forms.DateTimeField(label='Ida', widget=DatePicker())
    hr_ida = forms.TimeField(label='Hora ida', widget=TimePicker())
   



Lembrando que para utilizar é necessário importar os arquivos para que seja possível visualizar os layouts.

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6ji

"""
class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    ida = forms.DateTimeField(label='Ida', widget=DatePicker())
    hr_ida = forms.TimeField(label='Hora ida', widget=TimePicker())
    volta = forms.DateTimeField(label='Volta', widget=DatePicker())
    hr_volta = forms.TimeField(label='Hora ida', widget=TimePicker())