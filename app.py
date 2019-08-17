from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify, make_response
#from data import Articles
from flask_mysqldb import MySQL
from functools import wraps
import json
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kunci'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

app.config['SECRET_KEY'] ='thisisthesecretkey'

CORS(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') #http://127.0.0.1:5000/route?token=alsberJkaekfm233545ur

        if not token:
            return jsonify({'message' :'Token is missing!'}), 403
         
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message ' : 'Token is invalid'}), 403 

        return f(*args, **kwargs)
        
    return decorated

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'Gimanayah123':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

# Index
@app.route('/<kunci>', methods=['GET'])
@token_required
def index(kunci):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kunciku")
    rv = cur.fetchall()
    return jsonify(rv)

    cur.close()

if __name__ == '__main__':
    app.run(debug=True, port=80)