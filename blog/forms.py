from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25, message='username must be between 4 and 25 characters')])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password', message='passwords must match')])

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('This username already exists')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This email already exists')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')


class UpdateProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25, message='username must be between 4 and 25 characters')])
	email = StringField('Email', validators=[DataRequired(), Email()])