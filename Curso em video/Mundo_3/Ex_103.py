def ficha(jogador='<Desconhecido>', gols=0):
    return print(f'O jogador {jogador} fez {gols} gols no campeonato')

nome = str(input('Jogador: '))
qtd_gol = str(input('Gols: '))
if(qtd_gol.isnumeric()):
    qtd_gol = int(qtd_gol)
else:
    qtd_gol = 0

if(nome.strip() == ''): 
    ficha(gols=qtd_gol)
else:
    ficha(nome,qtd_gol)

