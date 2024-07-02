import os
import time
import psycopg2
from flask import Flask, render_template, request, g

app = Flask(__name__)

# Configuração do banco de dados
DATABASE = {
    'dbname': 'pdv',
    'user': 'postgres',
    'password': '123456',
    'host': 'db',
    'port': '5432'
}

# Conexão com o banco de dados
def connect_to_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=DATABASE['dbname'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                host=DATABASE['host'],
                port=DATABASE['port']
            )
            return conn
        except psycopg2.OperationalError as e:
            print("Database connection failed. Retrying in 5 seconds...")
            time.sleep(5)

# Abertura e fechamento de conexões
@app.before_request
def before_request():
    g.db = connect_to_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    consulta_resultado = None
    colunas = None
    erro = None

    if request.method == 'POST':
        comando_sql = request.form['comandoSQL']
        cursor = g.db.cursor()

        try:
            cursor.execute(comando_sql)
            rows = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]  # Obtém os nomes das colunas
            g.db.commit()
        except psycopg2.Error as e:
            erro = f"Erro ao executar a consulta: {e}"
            g.db.rollback()
            rows = []
        finally:
            cursor.close()

        consulta_resultado = rows

    return render_template('index.html', consulta_resultado=consulta_resultado, colunas=colunas, erro=erro)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
