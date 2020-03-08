bol_cont = True
lst_num = []
while (bol_cont):
    lst_num.append(int(input('Digite um número: ')))
    
    aux_val = input('Deseja continuar? [S/N]  ')
    if(aux_val.upper() == 'N'):
        bol_cont = False


print(f'{len(lst_num)}')
lst_num.sort()
lst_num.reverse()
print(f'{lst_num}')
print(f'{lst_num.__contains__(5)}')