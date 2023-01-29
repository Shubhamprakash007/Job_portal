from flask import render_template, url_for, flash, redirect, request
from job_portal import app, db, bcrypt
from job_portal.forms import RegistrationForm, LoginForm, ApplyForm, JobPostForm, ResumeForm
from job_portal.models import User, Employer, Resume, JobPost
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def home():
    jobs = JobPost.query.all()
    return render_template('home.html', jobs=jobs)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/resume", methods=["GET", "POST"])
def resume():
    form = ResumeForm()
    if form.validate_on_submit():
        resume = Resume(name=form.name.data,
                        email=form.email.data,
                        objective=form.objective.data,
                        experience=form.experience.data,
                        education=form.education.data,
                        skills=form.skills.data)
        db.session.add(resume)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('resume.html', form=form)

@app.route("/jobpost", methods=["GET", "POST"])
def jobpost():
    form = JobPostForm()
    if form.validate_on_submit():
        jobpost = JobPost(job_title=form.job_title.data,
                          company_name=form.company_name.data,
                          location=form.location.data,
                          job_description=form.job_description.data,
                          salary=form.salary.data,
                          experience_required=form.experience_required.data)
        db.session.add(jobpost)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('jobpost.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')




