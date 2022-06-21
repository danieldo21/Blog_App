from flask import render_template, url_for, flash, redirect, request
from main_app import app, db, bcrypt
from main_app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from main_app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# List of post dictionaries
posts = [ 
    
    {
      'author':'Daniel Do',      
      'title':'Blog Post 1',  
      'content':'First post content',
      'date_posted':'Febuary 4, 2022'   
    },
    
    {
      'author':'Danny',      
      'title':'Blog Post 2',  
      'content':'Second post content',
      'date_posted':'Febuary 8, 2022'   
    },
    
    {
      'author':'Danzo',      
      'title':'Blog Post 3',  
      'content':'Third post content',
      'date_posted':'Febuary 16, 2022'   
    }
    
]

#Routes

# Route for homepage
@app.route("/") #route to main page
@app.route("/home") #route to home page
def home():
    return render_template('home.html', posts=posts) # call to render the home page template

# Route for about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Route for registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

# Route for login page
@app.route("/login",  methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data): 
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check your email and password', 'danger')
  return render_template('login.html', title='Login', form=form)


# Route for login out
@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('home'))

@app.route("/account",  methods=['GET', 'POST'])
@login_required
def account():
  form = UpdateAccountForm()
  if form.validate_on_submit():
    current_user.username = form.username.data
    current_user.email = form.email.data
    db.session.commit()
    flash('Your account has been updated', 'success')
    return redirect(url_for('account'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
  image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
  return render_template('account.html', title='Account', image_file=image_file, form=form)