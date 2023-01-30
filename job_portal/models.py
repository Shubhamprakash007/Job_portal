from datetime import datetime
from job_portal import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))

# @login_manager.user_loader
# def load_employer(user_id):
#     return Employer.query.get(int(user_id))



class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Employer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    jobs = db.relationship('JobPost', backref='author', lazy=True)

    def __repr__(self):
        return f"Employer('{self.username}', '{self.email}')"


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    objective = db.Column(db.Text, nullable=False)
    experience = db.Column(db.Text, nullable=False)
    education = db.Column(db.Text, nullable=False)
    skills = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Resume('{self.name}')"

class JobPostForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(50), nullable=False)
    company_name = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location = db.Column(db.String(50), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    salary = db.Column(db.String(50), nullable=False)
    experience_required = db.Column(db.String(50), nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.job_title}', '{self.date_posted}')"


