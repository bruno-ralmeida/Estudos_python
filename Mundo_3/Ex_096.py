print('=-'*25)
print(f'{"Controle de terrenos":^50}')
print('=-'*25)

def area(l,c):
    return print(f'A área de um terreno {l}x{c} é de {l*c}m²')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l,c)