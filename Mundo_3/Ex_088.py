from random import randint
from time import sleep

print('-='*25,f'\n{"SURPRESINHA DA MEGA-SENA":^50}\n','-='*24)

qtd_jogos = int(input('Quantos jogos deseja realizar: '))
lst_jogos = list()
lst_aux = list()

for i in range(0, qtd_jogos):
    cont = 0
    while True:
        dado = randint(1,60)
        if(dado not in lst_aux):
            lst_aux.append(dado)
            cont += 1    
        if (cont >= 6):
            break
    lst_aux.sort()
    
    lst_jogos.append(lst_aux[:])
    lst_aux.clear()    

print('-='*25,f'\n{"Sorenteando...":^50}\n','-='*24)

for aposta in lst_jogos:
    print(aposta)
    sleep(1)

print('-='*25,f'\n{"Boa sorte...":^50}\n','-='*24)
