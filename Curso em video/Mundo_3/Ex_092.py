from datetime import date
ano_atual = date.today().year
dic_func = {}

dic_func['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dic_func['idade'] = ano_atual - nasc
dic_func['ctps'] = int(input('Carteria de trabalho (0 não tem): '))

if(dic_func['ctps'] != 0):
    dic_func['contratacao'] = int(input('Ano de contratação: '))
    dic_func['salario'] = float(input('Salário: '))
    dic_func['aposentadoria'] = dic_func['idade'] + (dic_func['contratacao'] + 35) - ano_atual

print('=-'*25)
for k, v in dic_func.items():
    print(f'- {k} tem valor {v}.')
