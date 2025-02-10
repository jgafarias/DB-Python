import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

# Cria uma conexão com o banco de dados 'Test.db' localizado no diretório 'DB-Python'
db = sqlite3.connect('DB-Python/Test.db')

cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

# Atualize os dados na tabela 'user'
cursor.execute('''UPDATE user
                  SET name = "Joao Gabriel", birthdate = "1996-06-24"
                  WHERE id = 1
                  ''')

# Alterado o nome de Joao Gabriel para Joao

db.commit()  # Confirma a transação no banco de dados

print('Dados atualizados com sucesso!')  # Imprime uma mensagem indicando que a atualização foi bem-sucedida
