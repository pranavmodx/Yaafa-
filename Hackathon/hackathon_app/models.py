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
    
    def json(self):
        return jsonify(
            id=id,
            topic_name=topic_name
        )
class subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(20), nullable=False)
    topics=db.Column(db.Text(30000),nullable=False)
    
    def json(self):
        a=topics.split(',')
        return jsonify(
            id=id,
            subject_name=subject_name,
            topics=a

        )

class Study_event(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    subject_name=db.Column(db.String(20),unique=True,nullable=False)
    topic_name=db.Column(db.String(20), nullable=False)
    pomodoro=db.Column(db.Boolean,nullable=False)
    ambient_music=db.Column(db.Boolean,nullable=False)
    intended_use=db.Column(db.Text(30000),nullable=False)
    _exit = db.Column(db.Boolean, nullable=False)
    proof_work=db.Column(db.Text(30000),nullable=False)
    summary = db.Column(db.Text(30000), nullable=False)
    time=db.Column(db.DateTime, nullable=False)
    def json(self):
        return jsonify(
            name=name,
            subject_name=subject_name,
            topic_name=topic_name,
            pomodoro=pomodoro,
            ambient_music=ambient_music,
            intended_use=intended_use,
            _exit=_exit,
            proof_work=proof_work,
            summary=summary,
            time=time
        )

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(20), nullable=False)
    book_level = db.Column(db.Integer, primary_key=True)

    def json(self):
        return jsonify(
            book_name=book_name,
            book_level=book_level
        )

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
    time=db.Column(db.DateTime,nullable=False)
    
    def json(self):
        return jsonify(
            id=id,
            name=name,
            topic_name=topic_name,
            book_name=book_name,
            pomodoro=pomodoro,
            ambient_music=ambient_music,
            intended_use=intended_use,
            _exit=_exit,
            proof_work=proof_work,
            no_of_probs=no_of_probs,
            summary=summary,
            time=time,
        )
class revise(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    topic_name=db.Column(db.String(20), nullable=False)
    last_checked_on = db.Column(db.String(20), nullable=False)
    pomodoro=db.Column(db.Boolean,nullable=False)
    ambient_music=db.Column(db.Boolean,nullable=False)
    intended_use=db.Column(db.Text(30000),nullable=False)
    _exit = db.Column(db.Boolean, nullable=False)
    proof_work=db.Column(db.Text(30000),nullable=False)
    summary = db.Column(db.Text(30000), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    def json(self):
        return jsonify(
            id=id,
            topic_name=topic_name,
            last_checked_on=last_checked_on,
            pomodoro=pomodoro,
            ambient_music=ambient_music,
            intended_use=intended_use,
            proof_work=proof_work,
            summary=summary,
            time=time,

        )



