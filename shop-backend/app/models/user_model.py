from app import db
class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   public_id= db.Column(db.String(100), unique=True)
   username = db.Column(db.String(100), unique=True)
   email= db.Column(db.String(100), unique=True)
   password = db.Column(db.String(300))
