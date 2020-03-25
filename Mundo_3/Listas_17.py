#Adiciona o elemento no final da lista
lst_comida = []
lst_comida.append('Pizza')
lst_comida.append('Bolo')
lst_comida.append('Coxinha')
lst_comida.insert(2,'Bolacha') # Inserindo na posição insert(n, elemento)
#Removendo elemento
print(lst_comida)
lst_comida.pop(1)
lst_comida.remove('Pizza')
print(lst_comida)

#Criando lista com range
lst_valores = list(range(5, 25, 3))
print(lst_valores)

#Ordenando a lista
lst_val = [9,5,4,10,5]
lst_val.sort()
print(lst_val)
#Lista Reversa
lst_val.reverse()
print(lst_val)

#Criando ligações em listas 
#Alterando a lista B tambem é alterado em A
a = [2,4,3,7]
b = a
b[2] = 0
print(f'A: {a}')
print(f'B: {b}')

#Copiando Listas
a = [2,4,3,7]
b = a[:] #É necessário indicar que você está copiando toda a lista
b[2] = 0
print(f'A: {a}')
print(f'B: {b}')