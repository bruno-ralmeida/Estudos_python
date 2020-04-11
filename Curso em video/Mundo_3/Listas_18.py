galera = [['Bruno', 22], ['Gustavo', 42], ['Maria', 25]]
#Mostrando todos os elementos
print(galera)
#Mostrando apenas os atributos do Bruno
print(galera[0])
#Mostrando apenas o nome Bruno
print(galera[0][0])

#Mostrando apenas o nome
for i in galera:
    print(i[0])

galera01 = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera01.append(dado[:])
    dado.clear() #Sempre lembrar de indicar que se trata de uma cópia, pois ao realizar 
                 #o comando cliar e eles tiverem uma ligação tudo será apagado.

print(galera01)