from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify
#from data import Articles
from flask_mysqldb import MySQL
from functools import wraps
import json
from flask_cors import CORS

app = Flask(__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kunci'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

CORS(app)

# Index
@app.route('/<kunci>', methods=['GET'])
def index(kunci):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kunciku")
    rv = cur.fetchall()
    return jsonify(rv)

    cur.close()

if __name__ == '__main__':
    app.run(debug=True)