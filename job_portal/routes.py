from flask import render_template, url_for, flash, redirect, request
from job_portal import app, db, bcrypt
from job_portal.forms import StudentRegistrationForm,EmployerRegistrationForm, StudentLoginForm, EmployerLoginForm, ApplyForm, JobPostForm, ResumeForm
from job_portal.models import Student, Employer, Resume, JobPostForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def home():
    jobs = JobPostForm.query.all()
    return render_template('home.html', jobs=jobs)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register_employer", methods=['GET', 'POST'])
def register_student():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = EmployerRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Employer(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register_student.html', title='Register', form=form)

@app.route("/register_student", methods=['GET', 'POST'])
def register_student():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Student(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login_student'))
    return render_template('register_student.html', title='Register', form=form)

@app.route("/login_student", methods=['GET', 'POST'])
def login_student():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = StudentLoginForm()
    if form.validate_on_submit():
        user = Student.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login_student.html', title='Login', form=form)

@app.route("/login_employer", methods=['GET', 'POST'])
def login_employer():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = EmployerLoginForm()
    if form.validate_on_submit():
        user = Employer.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login_employer.html', title='Login', form=form)

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
        jobpost = JobPostForm(job_title=form.job_title.data,
                          company_name=form.company_name.data,
                          location=form.location.data,
                          job_description=form.job_description.data,
                          salary=form.salary.data,
                          experience_required=form.experience_required.data)
        db.session.add(jobpost)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('jobpost.html', form=form)

@app.route("/apply", methods=['GET', 'POST'])
def apply():
    form = ApplyForm()
    if form.validate_on_submit():
        # Process form data and store it in a database or somewhere else
        flash('Your application has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('apply.html', title='Apply', form=form)

@app.route("/logout_student")
def logout_student():
    logout_user()
    return redirect(url_for('home'))

@app.route("/logout_employer")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')




