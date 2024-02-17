import flask
from flask import request, json, jsonify
import requests
import flask_mysqldb
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdocker'

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
  data = requests.get('https://randomuser.me/api')
  return data.json()

@app.route("/inserthost", methods=['POST', 'GET'])
def inserthost():
  data = requests.get('https://randomuser.me/api').json()
  username = data['results'][0]['name']['first']

#  try:
    # Estabelece uma conexão com o banco de dados
  mysql.init_app(app)
  cur = mysql.connection.cursor()
  
  # Executa a consulta de inserção
  cur.execute("""INSERT INTO users(name) VALUES(%s)""", (username,))
  
  # Confirma as alterações
  mysql.connection.commit()
  
  # Fecha o cursor
  cur.close()
  
  return username
#  except Exception as e:
    # Trata qualquer exceção que possa ocorrer durante a conexão ou execução da consulta
#    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port="8000")