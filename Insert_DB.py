from Connect_DB import connect  # Importa a função de conexão do módulo Connect_DB

db = connect()  # Estabelece a conexão usando a função do módulo Connect_DB
cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

# Adicionando dados à tabela 'user'
cursor.execute('''INSERT INTO user (id, name, birthdate) 
                  VALUES (
                      1, "Joao Gabriel", "1996-06-24"
                  )
                  ''')

db.commit()  # Confirma a transação no banco de dados

print('Dados inseridos com sucesso!')  # Imprime uma mensagem indicando que a inserção foi bem-sucedida
