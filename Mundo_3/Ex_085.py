lst_grp = [[],[]]

for i in range(1,8):
    
    dado = int(input(f'Digite o {i}º valor: '))
    if(dado % 2 == 0):
        lst_grp[0].append(dado)
    else:
        lst_grp[1].append(dado)
    
lst_grp[0].sort()
lst_grp[1].sort()
print(lst_grp)
print(f'Os valores pares foram {lst_grp[0]}')
print(f'Os valores impares foram {lst_grp[1]}')