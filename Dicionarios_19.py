#Declarção de Dicionários em Python 
dict_dados1 = dict() #Podemos utilizar dict()
dict_dados2 = {} #Podemos utilizar chaves

dict_dados2 = {'nome': 'Bruno', 'idade':22}
dict_dados2['sexo'] = 'M' #Incluindo elementos, em dicionários não existe o comando append()
print(dict_dados2['nome'])

filmes = {
            'titulo':'Start Wars', 
            'ano': 1977, 
            'diretor':'Geoge Lucas'
         }
print(filmes.values()) #Mostrando os elementos/valores de cada chave
print(filmes.keys()) #Mostrando as chaves 
print(filmes.items()) #Separa os elementos/valores com sua devida chave

for key, value in filmes.items():
    print(f'O {key} é {value}.')

#Combinando lista com dicionário
locadora = [{'titulo':'Start Wars', 
            'ano': 1977, 
            'diretor':'Geoge Lucas'}, 
            {'titulo':'Avengers',
            'ano': 2012,
            'diretor': 'Jose Whedon'}, 
            {'titulo':'Matrix',
            'ano': 1999,
            'diretor': 'Wachowski'
            }]

print(locadora[0]['ano'])
print(locadora[2]['titulo'])

lst_brasil = []
estado1 = {'uf': 'São Paulo', 'sigla':'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}

lst_brasil.append(estado1)
lst_brasil.append(estado2)

print(lst_brasil[0]['sigla'])

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #Para indicar que estamos copiando o elemento, utilizamos o método copy()
print(brasil)