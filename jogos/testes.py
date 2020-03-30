#Escrevendo em arquivos
"""arquivo = open('palavras.txt', 'w')
arquivo.write('Banana\n')
arquivo.write('Melancia\n')
arquivo.write('AbacaxI\n')
arquivo.write('Maçã\n')
arquivo.write('Pêra\n')
arquivo.write('Kiwi\n')
arquivo.write('Uva\n')
arquivo.write('Morango\n')
arquivo.close()"""

#Lendo o arquivo
arquivo = open('palavras.txt', 'r')
linha = arquivo.read() #Lê a primeira linha do arquivo
print(linha.strip())
#Exemplo

conteudo = arquivo.read()
print(conteudo)
conteudo = arquivo.read()
print(conteudo)
arquivo.close()