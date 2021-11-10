from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
#initialize the database
db = SQLAlchemy(app)

#create a db model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r' % self.id

@app.route("/")
def index():
    title = "The best page ever!"
    return render_template("index.html", title=title)

@app.route("/about")
def about():
    names = ["Jos", "Mary", "Tim"]
    return render_template("about.html", names=names)

#example of a page which can be a form
#you can add an HTTP method such as post for data
#there are request and response objects in flask
@app.route("/contact")
def contact():
    title="Welcome to my Contact Page!"
    return render_template("contact.html", title=title)

@app.route("/process", methods=['POST'])
def process():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    if not first_name or not last_name or not email: 
        error_statement = "Hey you there is an error..."
        return render_template("failure.html", error_statement=error_statement)

    title = "Thank you!"
    return render_template("process.html", 
    title=title, first_name=first_name, last_name=last_name, 
    email=email)
