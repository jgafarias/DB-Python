import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

  # Cria uma conexão com o banco de dados 'Test.db' localizado no diretório 'DB-Python'
db = sqlite3.connect('DB-Python/Test.db')

cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

# Cria a tabela 'user' com as colunas 'id', 'name' e 'birthdate'
cursor.execute('''CREATE TABLE user (
                      id INTEGER PRIMARY KEY NOT NULL, 
                      name VARCHAR(100) NOT NULL,  
                      birthdate DATE NOT NULL  
                  )''')

db.commit()  # Confirma a transação no banco de dados, criando a tabela

print('Tabela criada com sucesso!')  # Imprime uma mensagem indicando que a tabela foi criada com sucesso
