def fatorial(n, show=False):
    f = 1
    for c in range(n,0,-1):
        if(show):
            print(c, end=' ')
            if(c > 1):
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f*= c
    return f

def dobro(n):
    return n * 2


def area(l,c):
    return print(f'A área de um terreno {l}x{c} é de {l*c}m²')
