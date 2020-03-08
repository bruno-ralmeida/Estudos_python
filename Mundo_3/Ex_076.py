tpl_produtos = (
                'Arroz', 9.99,
                'Feijão', 4.99,
                'Macarrão', 2.49,
                'Alface', 1
                )
for pos in range(len(tpl_produtos)):
    if pos % 2 == 0:
        print(f'{tpl_produtos[pos]:.<30}', end=' ')
    else:
        print(f'R$ {tpl_produtos[pos]:<7.2f}')