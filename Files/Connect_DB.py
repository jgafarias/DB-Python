import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

def connect():
    return sqlite3.connect('Test.db')  # Retorna a conexão com o banco de dados
