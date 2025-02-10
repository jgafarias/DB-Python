from Connect_DB import connect  # Importa a função de conexão do módulo Connect_DB

db = connect()  # Estabelece a conexão usando a função do módulo Connect_DB
cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

# Exclui o registro na tabela 'user' onde o 'id' é igual a 1
cursor.execute('''DELETE FROM user
                  WHERE id = 1
                  ''')

db.commit()  # Confirma a transação no banco de dados

print('Dados excluídos com sucesso!')  # Imprime uma mensagem indicando que a exclusão foi bem-sucedida
