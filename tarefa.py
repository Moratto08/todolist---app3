# Importar a conexão criada
from conexao import get_conexao

# Importar a biblioteca psycopg2
from psycopg2.extras import RealDictCursor

# Importar jsonify do flask para retornar os dados no formato json
from flask import jsonify

def buscar_tarefas():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, nome, descricao FROM tarefas;"
    )
    # Buscar todos os registros na tabela
    tarefas = cursor.fetchall()

    # Fecha as conexôes
    cursor.close()
    conn.close()

    return jsonify(tarefas)