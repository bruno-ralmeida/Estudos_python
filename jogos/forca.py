def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_sec = 'batata'
    enforcou = False
    acertou = False
    palavra_chute = []

    while(not enforcou and not acertou):
        chute = input('Informe uma letra: ')

        if(palavra_sec.__contains__(chute) and not palavra_chute.__contains__(chute)):

            palavra_chute.append(chute)
            print(palavra_chute)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
