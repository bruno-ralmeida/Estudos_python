from time import sleep
def contador(*num):
    for i in range(1,11,1):
        print(i, end=' ', flush=True)
        sleep(0.25)

    print('Fim!')
    print('=-'*15)
    for i in range(10,-1,-2):
        print(i, end=' ', flush=True)
        sleep(0.25)
    
    print('Fim!')
    print('=-'*15)

    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if(p == 0):
        p = 1
    if(i > f):
        p *= -1
        f -=  1

    for i in range(i,f,p):
        print(i, end=' ', flush=True)
        sleep(0.25)

    print('Fim!')
    print('=-'*15)

contador()