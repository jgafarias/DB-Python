from Connect_DB import connect  # Importa a função de conexão do módulo Connect_DB

db = connect()  # Estabelece a conexão usando a função do módulo Connect_DB
cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

# Atualize os dados na tabela 'user'
cursor.execute('''UPDATE user
                  SET name = "JG", birthdate = "0000-00-00"
                  WHERE id = 1
                  ''')

# Alterado o nome de Joao Gabriel para Joao

db.commit()  # Confirma a transação no banco de dados

print('Dados atualizados com sucesso!')  # Imprime uma mensagem indicando que a atualização foi bem-sucedida
