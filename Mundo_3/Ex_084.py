galera = list()
dado = list()
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    
    if(len(galera) == 0):
        mai = men = dado[1]
    else:
        if(dado[1] < men):
            men = dado[1]
        if(dado[1] > mai):
            mai = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = input('Deseja continuar? [S/N] ')
    if resp in ('Nn'):
        break
    
print(len(galera))
print(f'O maior peso é {mai}KG. Peso de ', end='')
for i in galera:
    if(i[1] == mai):
        print(f'[{i[0]}]', end='')
   
print(f'\nO menor peso é {men}KG. Peso de ', end='')   
for i in galera:
    if(i[1] == men):
        print(f'[{i[0]}]', end='')
    