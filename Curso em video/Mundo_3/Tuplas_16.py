lanche = ('Pizza', 'Hamburguer', 'Refrigerante', 'Pudim', 'Batata')
#Mostra toda tupla
print(lanche)
#Mostra o elemento de acordo com o indice
print(lanche[2])
#Mostra o em ordem reversa
print(lanche[-2])
#Mostra os elementos do inicio até o limite de acordo com o indice
print(lanche[0:3])
#Mostra tudo após o indice informado
print(lanche[2:])
#Mostra tudo antes do indice informado
print(lanche[:2])
    
#Mostra a posicção e o elemento
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} que está na posição {pos}')


print('\n \n \n \n')