from flask import jsonify, request, abort,make_response
from app import db
from app import app
from app.models.user_model import User
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
import datetime

@app.route('/users',methods=['POST'])
def create_user():
   data = request.get_json()
   hashed_password = generate_password_hash(data['password'],method='sha256')
   new_user = User(public_id=str(uuid.uuid4()), username=data['username'],email=data['email'], password=hashed_password)
   db.session.add(new_user)
   db.session.commit()
   return jsonify({'message' :'New User has been created!'})


@app.route('/login')
def login():
   auth = request.authorization
   if not auth or not auth.username or not auth.password:
       return make_response('Could not verify ',401,{'WWW-Authenticate':'Basic realm="Login requierd!"'})
   user = User.query.filter_by(username=auth.username).first()
   if not user:
       return make_response(f'There is no user like {auth.username}',401,{'WWW-Authenticate':'Basic realm="Register requierd!"'})
   if check_password_hash(user.password,auth.password):
       token = jwt.encode({'public_id':user.public_id,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
       return jsonify({'token':token})
   return make_response('Could not verify ',401,{'WWW-Authenticate':'Basic realm="Login requierd!"'})
