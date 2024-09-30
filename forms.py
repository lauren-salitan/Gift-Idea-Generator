from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user is not present:
    #         raise ValidationError('Please use a different username.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is not present:
    #         raise ValidationError('Please use a different email address.')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user: 
            raise ValidationError('Username already in use. Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:  
            raise ValidationError('Email address already in use. Please use a different email address.')

class RecipientProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    birthday = DateField('Birthday')
    gender = StringField('Gender')
    relationship = StringField('Relationship', validators=[DataRequired()])
    interests = TextAreaField('Interests')
    occasion = StringField('Occasion')
    budget = FloatField('Budget')
    additional_details = TextAreaField('Additional Details')
    submit = SubmitField('Save Profile')
