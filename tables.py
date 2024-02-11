from application import application,db


with application.app_context():
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        age = db.Column(db.Integer)
        gender = db.Column(db.String(10))
        grades = db.relationship('SubjectGrade', backref='user', lazy=True)


    class SubjectGrade(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        subject = db.Column(db.String(100))
        # You can encrypt the grade column here
        grade = db.Column(db.String(100))

    db.create_all()
    
