from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True,index = True)
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  def __repr__(self):
    return f'User {self.username}'

