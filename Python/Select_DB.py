from Connect_DB import connect  # Importa a função de conexão do módulo Connect_DB

db = connect()  # Estabelece a conexão usando a função do módulo Connect_DB
cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

cursor = db.execute('''SELECT * FROM user''')  # Executa a consulta SQL para selecionar todos os registros da tabela 'user'

result = cursor.fetchall()  # Recupera todos os resultados da consulta e os armazena na variável 'result'

print(result)  # Imprime os resultados da consulta
