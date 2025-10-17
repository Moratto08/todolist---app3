# Importação das bibliotecas
from flask import Flask

# Cria o objeto do flask
app = Flask(__name__)

# Criando nossa primeira rota /api
@app.route('/api')
def index():
    return 'Api rodando'

# Identifica que é o arquivo principal e liga o servidor executando o flask 😊
if __name__== "__main__":
    app.run(debug=True)