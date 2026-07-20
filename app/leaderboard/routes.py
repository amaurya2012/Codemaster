from flask import Blueprint, render_template
from app.models import User, Submission
from app.extensions import db

leaderboard_bp = Blueprint("leaderboard", __name__)

@leaderboard_bp.route("/leaderboard")
def leaderboard():
    data = db.session.query(
        User.username,
        db.func.sum(Submission.score)
    ).join(Submission).group_by(User.username).all()
    return render_template("leaderboard/leaderboard.html", data=data)
