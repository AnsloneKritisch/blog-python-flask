from flask import Flask,render_template, Request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import confg.json
from datetime import datetime


local_server = True
app = Flask(__name__)
app.config.update( MAIL_SERVER = 'smtp.gmail.com'                          )

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phoneno = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date= db.Column(db.String(120), nullable=True)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/contact" , methods = [ ('GET') , ('POST')])
def contact():
    if (Request.method == 'POST') :
        ''' Add entry to the database'''
        name = Request.form.get('name')
        email = Request.form.get('email')
        phone = Request.form.get('phone')
        message = Request.form.get('message')
        entry = Contacts( name=name , email=email , phoneno=phone , message=message , date= datetime.now() )
        db.session.add(entry)
        db.session.commit()
        
    return render_template('contact.html')


@app.route("/start")
def start():
    return render_template('start.html')




app.run(debug=True)

