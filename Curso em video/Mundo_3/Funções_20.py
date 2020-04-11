#Função sem parametros
def mostraLinha():
    print('=-'*25)
#Função com parametros
def mostraMsg(msg):
  mostraLinha()
  print(f'{msg:^50}')
  mostraLinha()
  
mostraMsg('Hello World!')

def soma(a, b):
    return a + b

print(soma(3,5))

#Empacotamento de parametros
def contador(*num): #Definimos que podemos receber quantos parametros forem necessários 
    """
    Criando uma doc String
    Funcao criada por Bruno Rocha - 29/03/2020
    """
#-É criada uma tupla
    print(num)

contador(41,5,6,9,10)
contador(4,36,5)
contador()

def soma(a=0,b=0, c=0):
    """
    Parametros opcionais
    """
    return a + b + c

print(soma(12,5,3))

#Funções internas 
help(contador)
help(soma)