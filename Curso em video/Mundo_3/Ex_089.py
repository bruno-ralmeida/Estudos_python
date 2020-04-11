ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2) / 2

    ficha.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in('Nn'):
        break

print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*50)
for contador, aluno in enumerate(ficha):
    print(f'{contador:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-'*50)
    opc = int(input('Detalhes de nota? Informe o código do aluno (999 para sair). '))
    if(opc == 999):
        print(f'{"Finalizando...":^30}')
        break
    if(opc <= len(ficha)-1):
        print(f'Notas do aluno(a) {ficha[opc][0]} são {ficha[opc][1]}.')


