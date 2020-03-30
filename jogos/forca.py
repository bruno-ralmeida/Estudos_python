from random import randint

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open('jogos/palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    palavra_sec = palavras[randint(0, len(palavras))].upper()
    print(palavra_sec)
    
    enforcou = acertou = False
    lst_acerto = ['_' for letra in palavra_sec] #List Comprehension
    qtd_chute = len(palavra_sec) + 2

    while(not enforcou and not acertou):
        
        if(qtd_chute != 0):

            chute = str(input('\nInforme uma letra: ')).strip().upper()
            index = 0
            qtd_chute -= 1

            for letra in palavra_sec:
                if(chute == letra):
                    #print(f'Encontrei a lertra {chute} na posição {index+1}.')
                    lst_acerto[index] = letra
                    acertou = '_' not in lst_acerto 
                index += 1

            #Mostando as letras acertadas
            for i,v in enumerate(lst_acerto):
                if(i != len(lst_acerto)):
                    print(f'{v} ', end='')
                                
        else:
            print('\n\nEnforcou!')
            enforcou = True
        
                
            
    print("\nFim do jogo")

if(__name__ == "__main__"):
    jogar()
