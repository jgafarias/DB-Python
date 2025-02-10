import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

# Conecte ao banco de dados (ou crie um novo banco de dados)
db = sqlite3.connect('DB-Python/Test.db')  # Cria uma conexão com o banco de dados 'Test.db' localizado no diretório 'DB-Python'

cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados
cursor = db.execute('''SELECT * FROM user''')  # Executa a consulta SQL para selecionar todos os registros da tabela 'user'

result = cursor.fetchall()  # Recupera todos os resultados da consulta e os armazena na variável 'result'

print(result)  # Imprime os resultados da consulta
