from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps
# import pliku

app = Flask(__name__)

app.config['SECRET_KEY'] ='thisisthesecretkey'

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

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Aing teu ngarti!!'})

@app.route('/protected')
# @token_required
def protected():
    return jsonify({'message' : 'Cuman bisa dipake orang yang punya token bener!'})   

# @app.route('/api/<crot>',methods=['POST', 'GET'])
# @token_required
# def crot(crot):
#     if request.method=='POST':
#         msg = request.form['msg']
#         pwd = request.form['pwd']
#         return pliku.AESCipher(pwd).encrypt(msg).decode('utf-8')
#     else:
#       return "error"    

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    
if __name__ == '__main__':
    app.run(debug=True)