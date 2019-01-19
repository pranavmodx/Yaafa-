from hackathon_app import db, login_manager
from flask_login import UserMixin
db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class super_super_user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    students = db.Column(db.Text(30000), nullable=False)
    subject = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class super_user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    students=db.Column(db.Text(30000),nullable=False)
    subject=db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(20), nullable=False)

class subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(20), nullable=False)
    topics=db.Column(db.Text(30000),nullable=False)

class Study_event(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    topic_name=db.Column(db.String(20), nullable=False)
    pomodoro=db.Column(db.Boolean,nullable=False)
    ambient_music=db.Column(db.Boolean,nullable=False)
    intended_use=db.Column(db.Text(30000),nullable=False)
    _exit = db.Column(db.Boolean, nullable=False)
    proof_work=db.Column(db.Text(30000),nullable=False)
    summary = db.Column(db.Text(30000), nullable=False)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(20), nullable=False)
    book_level = db.Column(db.Integer, primary_key=True)

class problem_event(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    topic_name=db.Column(db.String(20), nullable=False)
    book_name=db.Column(db.String(20), nullable=False)
    pomodoro=db.Column(db.Boolean,nullable=False)
    ambient_music=db.Column(db.Boolean,nullable=False)
    intended_use=db.Column(db.Text(30000),nullable=False)
    _exit = db.Column(db.Boolean, nullable=False)
    proof_work=db.Column(db.Text(30000),nullable=False)
    no_of_probs = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.Text(30000), nullable=False)

class revise(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    topic_name=db.Column(db.String(20), nullable=False)
    last_checked_on = db.Column(db.String(20), nullable=False)
    pomodoro=db.Column(db.Boolean,nullable=False)
    ambient_music=db.Column(db.Boolean,nullable=False)
    intended_use=db.Column(db.Text(30000),nullable=False)
    _exit = db.Column(db.Boolean, nullable=False)
    proof_work=db.Column(db.Text(30000),nullable=False)
    summary = db.Column(db.Text(30000), nullable=False)

