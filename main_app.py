from flask import Flask, render_template, url_for
app = Flask(__name__)



app.config['SECRET KEY'] = 'e512e9952e4e59843203abecb8e461a2'



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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__=='__main__':
    app.run(debug=True)