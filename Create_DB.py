import sqlite3

# Conecte ao banco de dados (ou crie um novo banco de dados)
db = sqlite3.connect('DB-Python/Test.db')

cursor = db.cursor()
cursor = db.execute('''CREATE TABLE user (
                            id INTEGER PRIMARY KEY NOT NULL,
                            name VARCHAR(100) NOT NULL,
                            birthdate DATE NOT NULL
                    )''')

db.commit()

print('Tabela criada com sucesso!')