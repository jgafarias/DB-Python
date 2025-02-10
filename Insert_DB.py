import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

# Cria uma conexão com o banco de dados 'Test.db' localizado no diretório 'DB-Python'
db = sqlite3.connect('DB-Python/Test.db')

cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

# Adicionando dados à tabela 'user'
cursor.execute('''INSERT INTO user (id, name, birthdate) 
                  VALUES (
                      1, "Joao Gabriel", "1996-06-24"
                  )
                  ''')

db.commit()  # Confirma a transação no banco de dados

print('Dados inseridos com sucesso!')  # Imprime uma mensagem indicando que a inserção foi bem-sucedida
