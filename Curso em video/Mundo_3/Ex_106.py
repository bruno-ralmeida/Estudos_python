tpl_cor = (
        '\033[1;31m' ,#0 VERMELHO
        '\033[1;32m' ,#1 VERDE
        '\033[1;34m' ,#2 AZUL
        '\033[1;35m' ,#3 MAGENTA
        '\033[1;37m' ,#4 CINZA CLARO
        '\033[1;33m' #5 AMARELO
        )

def ajuda(com):
    titulo(f'Acessando o manual do cmando \'{com}\'', 4)
    print(tpl_cor[2], end='')
    help(com)
    print(tpl_cor[0], end='')

def titulo(msg, cor=0):
    tam = len(msg)
    print(tpl_cor[cor], end='')
    print('-='* tam)
    print(f'{msg:^}')
    print('-='* tam)
    print(tpl_cor[cor], end='')

while True:
    titulo('Sistema de ajuda PyHelp', 0)
    comando = str(input('Função ou Biblioteca >'))
    if(comando.upper() == 'FIM'):
        break
    else:
        ajuda(comando)
titulo('Até logo!', 2)

