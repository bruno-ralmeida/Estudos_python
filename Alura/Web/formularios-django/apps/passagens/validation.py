def verifica_org_des(origem, destino, lst_erros):
    """Verificar se origem e destino são iguais."""
    if origem == destino:
        lst_erros['destino'] = 'Origem e destino não podem ser iguais' #Indicamos o campo que o erro será exibido e atribuimos a mensagem

def verifica_numeros(valor_campo, nome_campo, lst_erros):
    """Função para verificar se existem digito numericos."""
    if any(char.isdigit() for char in valor_campo):
        lst_erros[nome_campo] = 'Não inclua números neste campo'