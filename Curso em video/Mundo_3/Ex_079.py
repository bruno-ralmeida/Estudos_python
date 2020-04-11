bol_cont = True
lst_num = []
while (bol_cont):
    aux_num = int(input('Digite um número: '))
    
    if(not lst_num.__contains__(aux_num)):
        lst_num.append(aux_num)
        lst_num.sort()
        print('Número adicionado.')
    else:
        print('Número não adicionado.')

    aux_val = input('Deseja continuar? [S/N]  ')
    if(aux_val.upper() == 'N'):
        bol_cont = False

print(lst_num)