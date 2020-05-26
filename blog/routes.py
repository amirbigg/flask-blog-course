from flask import render_template, redirect, url_for, flash
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash('you registered successfully', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)