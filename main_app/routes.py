from flask import render_template, url_for, flash, redirect 
from main_app import app, db, bcrypt
from main_app.forms import RegistrationForm, LoginForm
from main_app.models import User, Post

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
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data): 
    
    
    flash('Login Failed. Please check your username and password', 'danger')
  return render_template('login.html', title='Login', form=form)