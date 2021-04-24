from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile
from flask_login import login_required
from ..models import User
from .. import db

@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  title = 'Pitch'

  return render_template('index.html',title = title)


@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
  form = PitchForm()
  # my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
  if form.validate_on_submit():
    description = form.description.data
    title = form.title.data
    owner_id = current_user
    category = form.category.data
    print(current_user._get_current_object().id)
    new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
    db.session.add(new_pitch)
    db.session.commit()
        
        
    return redirect(url_for('main.index'))
  return render_template('pitches.html',form=form)

@main.route('/user/<uname>')
@login_required
def profile(uname):
  categories = Category.query.all()
  user = User.query.filter_by(username = uname).first()
  title = current_user.username + " | Pitch"
  if user is None:
    abort(404)
  pitches = Pitch.get_user_pitch(user.id)
  return render_template("profile/profile.html", user = user, categories=categories, pitches=pitches, title=title)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()
  categories = Category.query.all()
  if user is None:
    abort(404)
    
  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data
  
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form =form)