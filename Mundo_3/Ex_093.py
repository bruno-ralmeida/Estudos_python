dic_jogador = {}
dic_jogador['nome'] = str(input('Nome do jogador: ')) 
qtd_jg = int(input(f'Quantas partidas {dic_jogador["nome"]} jogou? '))
lst_gol = []

for i in range(0, qtd_jg):
    gol = int(input(f'Quantos gols na partida {i}: '))
    lst_gol.append(gol)
dic_jogador['gols'] = lst_gol
dic_jogador['total'] = sum(lst_gol)

print('-='*25)

for k, v in dic_jogador.items():
    print(f'- O {k} tem valor {v}.')