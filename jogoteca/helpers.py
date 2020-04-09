import os
from jogoteca import app


def recupra_imagem(id):
    # Retorna os arquivos em algum diretório
    for nome_arquivo in os.listdir(app.config["UPLOAD_PATH"]):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

def excluir_imagem(id):
    arquivo = recupra_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))