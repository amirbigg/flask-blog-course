from flask import render_template
from blog import app


@app.route('/')
def routes():
	return render_template('home.html')