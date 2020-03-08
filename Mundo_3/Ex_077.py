tpl_palavras = (
                'Professor', 'Dia Triste', 'Python',
                'Trap', 'Programador', 'Cientista de dados'
                )
for p in tpl_palavras:
    print(f'\nNa palavra {p} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')