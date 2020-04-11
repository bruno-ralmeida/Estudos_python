lst_num = []
maior = menor = None
for i in range(0,5):
    lst_num.append(int(input('Digite um número: ')))

    if i == 0:
        maior = menor = lst_num[i]
    else: 
        if lst_num[i] > maior:
            maior = lst_num[i]
        elif (lst_num[i] < menor):
            menor = lst_num[i]

print('=-' * 30)
print(f'A lista: {lst_num}')

print(f'O menor valor é {min(lst_num)} e está na posição ', end= '')
for pos, item in enumerate(lst_num):
    if (item == menor):
        print(f'{pos}...', end=' ')

print(f'\nO maior valor é {max(lst_num)} e está na posição ', end= '')
for pos, item in enumerate(lst_num):
    if (item == maior):
        print(f'{pos}...', end=' ')