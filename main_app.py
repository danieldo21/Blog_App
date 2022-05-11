# This is a blog app that allows users to register and post blogs
from enum import unique
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'e512e9952e4e59843203abecb8e461a2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.string(20), unique=True, nullable=False)
  email = db.Column(db.string(120), unique=True, nullable=False)
  image_file = db.Column(db.string(20), nullable=False, default='default.jpg')
  password = db.Column(db.string(60), nullable=False)
  
  def __repr__(self):
    return f"User('{self.username}','{self.email}','{self.image_file}') "

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
      flash(f'Account created for {form.username.data}!', 'success')
      return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# Route for login page
@app.route("/login",  methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Failed. Please check your username and password', 'danger')
  return render_template('login.html', title='Login', form=form)

# Allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)
