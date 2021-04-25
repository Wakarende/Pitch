from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from sqlalchemy.sql import func

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

class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.Text(),nullable = False)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

  def save_c(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,pitch_id):
    comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    return comments

    
  def __repr__(self):
    return f'comment:{self.comment}'

class Upvote(db.Model):
  __tablename__ = 'upvotes'

  id = db.Column(db.Integer,primary_key=True)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_upvotes(cls,id):
    upvote = Upvote.query.filter_by(pitch_id=id).all()
    return upvote


  def __repr__(self):
    return f'{self.user_id}:{self.pitch_id}'

class Downvote(db.Model):
  __tablename__ = 'downvotes'

  id = db.Column(db.Integer,primary_key=True)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_downvotes(cls,id):
    downvote = Downvote.query.filter_by(pitch_id=id).all()
    return downvote

  def __repr__(self):
    return f'{self.user_id}:{self.pitch_id}'