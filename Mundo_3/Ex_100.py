from time import sleep
from random import randint
def sorteio():
    lst_aux = []
    for i in range(0,5):
        dado = randint(1,10)
        lst_aux.append(dado)
        print(f'Valor sorteado: {dado} ', flush=True )
        sleep(0.25)
    print('~'*25)
    return lst_aux



def somaPar(lista):
    
    soma = 0
    for i in lista:
        if(i % 2 == 0):
            soma += i

    return soma

print(somaPar(sorteio()))

