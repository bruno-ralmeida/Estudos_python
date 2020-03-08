tpl_num = ('zero', 'um' ,'dois' ,'três' ,'quatro' ,'cinco' ,'seis' ,'sete' ,'oito' ,'nove' ,'dez' ,'onze' ,
           'doze' ,'treze' , 'quatorze', 'quinze' ,'dezesseis' ,'dezessete', 'dezoito' ,'dezenove', 'vinte' )

num_dig = int(input('Digite um número entre 0 e 20: '))
valido = False


while (valido == False):
    if ((num_dig >= 0) and (num_dig <= 20)):
        valido = True
        print(tpl_num[num_dig])
        break
    num_dig = int(input('Numero invalido. Digite um número entre 0 e 20: '))

