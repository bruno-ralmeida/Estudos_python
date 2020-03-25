matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = scol = mai = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Informe o valor [{l}][{c}]: '))
    
for l in range(0,3):
    scol += matriz[l][2]
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='') #:^5 comando de 5 casas com alinhamento centralizado
        if(matriz[l][c] % 2 == 0):
            spar += matriz[l][c]
        if(c == 0):
            mai = matriz[1][c]
        elif(matriz[1][c] > mai):
            mai = matriz[1][c]
    print()

print(f'A soma dos valore pares é {spar}.')
print(f'A soma da terceira coluna é {scol}.')
print(f'O maior número da segunda coluna é {mai}.')
