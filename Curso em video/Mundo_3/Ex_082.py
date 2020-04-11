bol_cont = True
lst_num = [] 
lst_par = [] 
lst_imp = []
while (bol_cont):
    aux_num = int(input('Digite um número: '))
    
    lst_num.append(aux_num)

    if(aux_num % 2 == 0):
        lst_par.append(aux_num)
    else:
        lst_imp.append(aux_num)

    aux_val = input('Deseja continuar? [S/N]  ')
    if(aux_val.upper() == 'N'):
        bol_cont = False

print(lst_num)
print(lst_par)
print(lst_imp)