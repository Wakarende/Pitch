from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True,index = True)
  pass_secure = db.Column(db.String(255))
  pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
  profile_pic_path = db.Column(db.String())
  # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  def __repr__(self):
    return f'User {self.username}'

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

class Pitch(db.Model):
  '''
  '''
  __tablename__ = 'pitches'

  id = db.Column(db.Integer, primary_key = True)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  description = db.Column(db.String(), index = True)
  title = db.Column(db.String())
    # downvotes = db.Column(db.Integer, default=int(0))
    # upvotes = db.Column(db.Integer, default=int(0))
  category = db.Column(db.String(255), nullable=False)
  # comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
  # upvotes = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
  # downvotes = db.relationship('Downvote', backref = 'pitch', lazy = 'dynamic')

    
  @classmethod
  def get_pitches(cls, id):
    pitches = Pitch.query.order_by(pitch_id=id).desc().all()
    return pitches

  def __repr__(self):
    return f'Pitch {self.description}'