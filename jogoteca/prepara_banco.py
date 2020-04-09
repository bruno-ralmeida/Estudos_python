import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='localhost', port=3306)

# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `jogoteca`;")
#conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `jogoteca` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `jogoteca`;
    CREATE TABLE `jogo` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `categoria` varchar(40) COLLATE utf8_bin NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `usuario` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `nome` varchar(20) COLLATE utf8_bin NOT NULL,
      `senha` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
#Inserindo dados atráves de lista de tuplas
cursor.executemany(
      'INSERT INTO jogoteca.usuario (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('xxnbr', 'Bruno Rocha', '1234'),
            ('aninha', 'Ana Carolina Martins', '1234'),
            ('bia99', 'Bianca Rocha', '1999')
      ])

cursor.execute('select * from jogoteca.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
      'INSERT INTO jogoteca.jogo (nome, categoria, console) VALUES (%s, %s, %s)',
      [
            ('God of War 4', 'Acao', 'PS4'),
            ('NBA 2k18', 'Esporte', 'Xbox One'),
            ('Rayman Legends', 'Indie', 'PS4'),
            ('Super Mario RPG', 'RPG', 'SNES'),
            ('Super Mario Kart', 'Corrida', 'SNES'),
            ('Fire Emblem Echoes', 'Estrategia', '3DS'),
      ])

cursor.execute('select * from jogoteca.jogo')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senÃ£o nada tem efeito
conn.commit()
cursor.close()