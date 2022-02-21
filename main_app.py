from flask import Flask, render_template
app = Flask(__name__)

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
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True)