from flask import Flask, render_template ,request
import json
from flask_mail import Mail , Message


with open('config.json', 'r') as c:
    par = json.load(c)["par"]



app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com' ,
    MAIL_PORT = '465' ,
    MAIL_USE_SSL = True ,
    MAIL_USERNAME = par['gmail-user'] ,
    MAIL_PASSWORD = par['gmail-password']
                  )
mail = Mail(app)

@app.route("/")
def home():
    return render_template('index.html' , par=par)


@app.route("/about")
def about():
    return render_template('about.html'  , par=par)


@app.route("/post")
def post():
    return render_template('post.html'  , par=par)


@app.route("/contact")
def contact():

    return render_template('contact.html'  , par=par)


@app.route("/start")
def start():
    return render_template('start.html'  , par=par)


app.run(debug=True)

