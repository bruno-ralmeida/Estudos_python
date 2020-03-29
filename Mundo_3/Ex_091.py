from random import randint
from time import sleep
from operator import itemgetter

dic_dados = {}
for i in range(0,4):
    dic_dados[f'jogador {i}'] = randint(1,6)

ranking = sorted(dic_dados.items(), key=itemgetter(1), reverse=True)

for k, v in dic_dados.items():
    sleep(0.5)
    print(f'- O {k} tirou {v}.')
print('-='*25)
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1}º lugar {v[0]} tirou {v[1]} no dado.')

