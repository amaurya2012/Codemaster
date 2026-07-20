from flask_login import UserMixin
from datetime import datetime
from .extensions import db

# =========================
# USER MODEL
# =========================
class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), default="user")

    submissions = db.relationship("Submission", backref="user", lazy=True)


# =========================
# PROBLEM MODEL
# =========================
class Problem(db.Model):
    __tablename__ = "problem"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)

    # 🔥 MARKS PER QUESTION
    marks = db.Column(db.Integer, nullable=False, default=10)

    # Visible to users
    sample_input = db.Column(db.Text)
    sample_output = db.Column(db.Text)

    # Public test cases
    input_data = db.Column(db.Text, nullable=False)
    expected_output = db.Column(db.Text, nullable=False)

    # 🔒 Hidden test cases (NOT visible to users)
    hidden_input = db.Column(db.Text, nullable=False)
    hidden_output = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    submissions = db.relationship("Submission", backref="problem", lazy=True)


# =========================
# SUBMISSION MODEL
# =========================
class Submission(db.Model):
    __tablename__ = "submission"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Text, nullable=False)

    language = db.Column(db.String(20), nullable=False)

    status = db.Column(db.String(30), default="Pending")
    score = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey("problem.id"), nullable=False)

    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
