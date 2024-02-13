from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()


# User Table to store user Entries.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    grades = db.relationship('SubjectGrade', backref='user', lazy=True)


# Subject Grades Table to store Grade Entries.
class SubjectGrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(100))
    grade = db.Column(db.String(20480000000000))


