from random import randint


def jogar():
    msg('Bem vindo ao jogo da Forca!')
    palavra_sec = sortear_palavra()

    # Regras
    enforcou = acertou = False
    lst_acerto = ['_' for letra in palavra_sec]  # List Comprehension
    erros = 0

    while not enforcou and not acertou:
        erros = verifica_chute(palavra_sec, lst_acerto, erros)
        if erros != 7:
            acertou = verifica_ganhador(lst_acerto)
            mostra_acerto(lst_acerto)
        else:
            enforcou = True

    if acertou:
        msg_vencedor()
    elif enforcou:
        msg_perdedor(palavra_sec)
    msg('Fim de Jogo.')


def msg(txt_msg):
    print('\n')
    print('-=' * 25)
    print(f'{txt_msg:^50}')
    print('-=' * 25)


def msg_vencedor():
    print('')
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def msg_perdedor(palavra_secreta):
    print("Você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print('')


def sortear_palavra():
    # Definiando a palavra
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    palavra_sec = palavras[randint(0, len(palavras))].upper()
    return palavra_sec


def verifica_chute(palavra_sec, lst_acerto, erros):
    chute = str(input('\nInforme uma letra: ')).strip().upper()
    index = 0

    for letra in palavra_sec:
        if (chute == letra):
            lst_acerto[index] = letra
        index += 1
    if chute not in palavra_sec:
        erros += 1
        desenha_forca(erros)




    return erros


def verifica_ganhador(lst_acerto):
    acertou = '_' not in lst_acerto
    return acertou

def mostra_acerto(lst_acerto):
    # Mostando as letras acertadas
    for i, v in enumerate(lst_acerto):
        if i != len(lst_acerto):
            print(f'{v} ', end='')


if __name__ == "__main__":
    jogar()
