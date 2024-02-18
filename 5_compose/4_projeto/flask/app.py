import flask
from flask import Flask, request, render_template, json, jsonify
import requests
import mysql.connector

app = flask.Flask(__name__)
app.config["DEBUG"] = True

database=mysql.connector.connect(host='db',user='root',passwd='jamaica',database='flaskdocker')

@app.route("/", methods=["GET"])
def index():
  data = requests.get('https://randomuser.me/api')
  return data.json()

@app.route("/inserthost", methods=['POST', 'GET'])
def inserthost():
  data = requests.get('https://randomuser.me/api').json()
  username = data['results'][0]['name']['first']

  cursor=database.cursor()
  cursor.execute("""INSERT INTO users(name) VALUES(%s)""", (username,))
  database.commit()

  return username

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port="5000")