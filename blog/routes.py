from flask import render_template
from blog import app
from blog.forms import RegistrationForm, LoginForm


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)