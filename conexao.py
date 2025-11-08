# Importar as bibliotecas
import psycopg2
from dotenv import load_dotenv

#Importar o modulo OS do python
import os

#Carregar o arquivo env
load_dotenv():

# Função que retorna a conexão com banco de dados postgres
def get_conexao():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_DATABASE'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=5432('DB_POR'),

    )
    return conn