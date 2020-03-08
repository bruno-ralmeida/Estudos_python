bol_cont = True
lst_num = []

for c in range(0,5):
    aux_num = int(input('Digite um número: '))
   
    if((len(lst_num) == 0) or (aux_num > lst_num[-1])): #Se o número for maior que o utlitmo
       lst_num.append(aux_num)
    else: 
        pos = 0
        while pos < len(lst_num):
            if(aux_num <= lst_num[pos]):
                lst_num.insert(pos, aux_num)
                break
            pos += 1
print('-=' * 30)
print(lst_num)