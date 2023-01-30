from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from job_portal.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ResumeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    objective = TextAreaField('Objective', validators=[DataRequired()])
    experience = TextAreaField('Work Experience', validators=[DataRequired()])
    education = TextAreaField('Education', validators=[DataRequired()])
    skills = TextAreaField('Skills', validators=[DataRequired()])
    submit = SubmitField('Submit')

class JobPostForm(FlaskForm):
    job_title = StringField('Job Title', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    job_description = TextAreaField('Job Description', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    experience_required = StringField('Experience Required', validators=[DataRequired()])
    submit = SubmitField('Post Job')
   

class ApplyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    resume = StringField('Resume', validators=[DataRequired()])
    submit = SubmitField('Apply')


