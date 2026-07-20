from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.extensions import db, login_manager

auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password_hash, request.form["password"]):
            login_user(user)

            # 🔥 ROLE-BASED REDIRECT (THIS IS THE FIX)
            if user.role == "admin":
                return redirect(url_for("admin.admin_dashboard"))
            else:
                return redirect(url_for("user.dashboard"))

    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u = User(
            username=request.form["username"],
            email=request.form["email"],
            password_hash=generate_password_hash(request.form["password"])
        )
        db.session.add(u)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
