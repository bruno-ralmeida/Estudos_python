from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe

class PassagemForms(forms.Form):
	origem = forms.CharField(label='Origem', max_length=100)
	destino = forms.CharField(label='Destino', max_length=100)
	data_ida = forms.DateField(label='Data Ida', widget=DatePicker(
		options={
			'minDate': 'moment',
			'useCurrent': True,}
			))
	hr_ida = forms.TimeField(label='Hora ida', widget=TimePicker(
		options={
			'format':'LT'
			}
		))
	data_volta = forms.DateField(label='Data Volta', widget=DatePicker())
	hr_volta = forms.TimeField(label='Hora ida', widget=TimePicker(
		options={
			'format':'LT'
			}
		))
	data_pesquisa = forms.DateField(label='Data de Pesquisa', disabled=True, initial=datetime.today())
	classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
	info = forms.CharField(label='Informações', max_length=200,required=False, widget=forms.Textarea())
	email = forms.EmailField(label='E-mail', max_length=150)