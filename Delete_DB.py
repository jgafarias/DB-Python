import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

# Cria uma conexão com o banco de dados 'Test.db' localizado no diretório 'DB-Python'
db = sqlite3.connect('DB-Python/Test.db')

cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

# Exclui o registro na tabela 'user' onde o 'id' é igual a 1
cursor.execute('''DELETE FROM user
                  WHERE id = 1
                  ''')

db.commit()  # Confirma a transação no banco de dados

print('Dados excluídos com sucesso!')  # Imprime uma mensagem indicando que a exclusão foi bem-sucedida
