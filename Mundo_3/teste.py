"""o total de faltas do campeonato
o time que fez mais faltas
o time que fez menos faltas

mat_times = [ 
            ['Brasil', 'Italia', [10, 9] ], 
            ['Brasil', 'Espanha', [ 5, 7] ], 
            ['Italia', 'Espanha', [ 7, 8] ]  
            ]

tot_faltas = 0

for pos,time in enumerate(mat_times):
    #Total de Faltas
    aux_tot = sum(mat_times[pos-1][2])
    tot_faltas += aux_tot
    #Time com mais faltas
    aux_time = mat_times[pos]
    time_01 = aux_time[0]
    time_02 = aux_time[1]
    aux_falta = aux_time[2]
    teste = [time_01, aux_falta[0]]
    teste_02 = [time_02, aux_falta[1]]
    print(teste_02.sort())
    print(teste.sort())

print(f'Total de faltas no campeonato é {tot_faltas}.')"""
