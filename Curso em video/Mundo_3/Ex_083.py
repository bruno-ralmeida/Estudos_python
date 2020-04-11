val = input('Digite um expressão: ')
if(val.count('(') != val.count(')')):
    print('Expressão incorreta.')
else:
    print('Expressão correta.')