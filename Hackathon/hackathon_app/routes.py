from hackathon_app import app, db
from flask import render_template, flash, redirect, url_for
from hackathon_app.forms import RegistrationForm, LoginForm, StudyForm
from hackathon_app.models import User
from flask_login import login_user, logout_user, current_user, login_required
from hackathon_app import bcrypt


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('You have registered successfully.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form, title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have logged in successfully.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/student')
def student():
    return render_template('student.html', title='Student')


@app.route('/student/study')
def study():
    form = StudyForm()

    if form.validate_on_submit():
        flash('You have logged in successfully.', 'success')
        return redirect(url_for('student'))
    else:
        flash('Login unsuccessful. Please check email and password', 'danger')

    return render_template('student_study.html', form=form, title='Login')


@app.route('/student/solve')
def solve():
    return render_template('student_solve.html', title='Solve')


@app.route('/student/revise')
def revise():
    return render_template('student_revise.html', title='Revise')


@app.route('/teacher')
def teacher():
    return render_template('teacher.html', title='Teacher')


@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html', title='Pomodoro')

