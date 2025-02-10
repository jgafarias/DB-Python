from Connect_DB import connect  # Importa a função de conexão do módulo Connect_DB

db = connect()  # Estabelece a conexão usando a função do módulo Connect_DB
cursor = db.cursor()  # Cria um objeto cursor para interagir com o banco de dados

# Cria a tabela 'user' com as colunas 'id', 'name' e 'birthdate'
cursor.execute('''CREATE TABLE user (
                      id INTEGER PRIMARY KEY NOT NULL,  # Coluna 'id' como chave primária não nula
                      name VARCHAR(100) NOT NULL,  # Coluna 'name' como string de no máximo 100 caracteres e não nula
                      birthdate DATE NOT NULL  # Coluna 'birthdate' como data e não nula
                  )''')

db.commit()  # Confirma a transação no banco de dados, criando a tabela

print('Tabela criada com sucesso!')  # Imprime uma mensagem indicando que a tabela foi criada com sucesso
