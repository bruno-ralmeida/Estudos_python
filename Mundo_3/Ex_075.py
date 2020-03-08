tpl_int = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'{tpl_int.count(9)}')
if(tpl_int.__contains__(3)):
    print(f'{tpl_int.index(3)}')
else:
    print('Não existe nenhum número 3')
print('Os valores pares digitados foram: ', end='')
for n in tpl_int:
    if n % 2 == 0:
        print(n, end=' ')


