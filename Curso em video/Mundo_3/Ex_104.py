def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if(n.isnumeric()):
            valor = int(n)
            break
        else:
            print('\033[0;31mErro! Digite um número válido.\033[m')
        
    return valor

n = leiaInt('Digite um número: ')
print(f'O número digitado foi {n}.')