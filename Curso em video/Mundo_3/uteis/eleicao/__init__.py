from datetime import date

def voto(ano):
    ano_atual = date.today().year
    idade =  ano_atual - ano
    if((idade < 16)):
        r = 'NÃO VOTA'    
    elif(((idade >= 16) and (idade < 18)) or (idade >= 65)):
        r = 'VOTO OPCIONAL'
    else:
        r = 'VOTO OBRIGATÓRIO'
    return f'Com {idade} anos: {r}'