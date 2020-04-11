"""
FAÇA UM PROGRAMA QUE LEIA O NOME E MÉDIA DO ALUNO, GUARDANDO 
TAMBEM A SITUAÇÃ EM UM DICIONÁRIO. NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA
"""
dic_aluno = {}
sit_aluno = None
dic_aluno['aluno'] = str(input('Informe o nome do aluno: '))
dic_aluno['media'] = float(input(f'Informe a media do aluno {dic_aluno["aluno"]}: '))
if(dic_aluno['media'] < 5):
    sit_aluno = 'Reprovado'
elif(dic_aluno['media'] >= 7):    
    sit_aluno = 'Aprovado'
else:
    sit_aluno = 'Em recuperação'    
dic_aluno['situacao'] = sit_aluno

for k, v in dic_aluno.items():
    print(f'- {k} é igual {v}.')