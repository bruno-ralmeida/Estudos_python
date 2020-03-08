tpl_times = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional', 'Chapecoense',
             'Corinthians', 'Fortaleza EC','Goiás','Bahia','Vasco da Gama','Atlético-MG','Fluminense',
             'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',	'Avaí')


print(f'-' * 50)
print(f'Os 5 primeiros colocados são: {tpl_times[0:5]}')
print(f'-' * 50)
print(f'Os 4 últimos são {tpl_times[-4:]}')
print(f'-' * 50)
print(f'A ordem alfabetica dos times são: {sorted(tpl_times)}')
print(f'-' * 50)
print(f'O Chapeconence está na {tpl_times.index("Chapecoense") + 1}ª posião')