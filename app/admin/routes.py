from flask import Blueprint, render_template, request, redirect, url_for, send_file
from flask_login import login_required, current_user
from app.models import Problem, Submission, User
from app.extensions import db
import csv
import io

# =====================================================
# ADMIN BLUEPRINT (ONLY ONE)
# =====================================================
admin_bp = Blueprint("admin", __name__)

# =====================================================
# ADMIN DASHBOARD
# =====================================================
@admin_bp.route("/admin")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        return "Forbidden", 403
    return render_template("admin/dashboard.html")

# =====================================================
# MANAGE PROBLEMS (ADD + LIST)
# =====================================================
@admin_bp.route("/admin/problems", methods=["GET", "POST"])
@login_required
def manage_problems():
    if current_user.role != "admin":
        return "Forbidden", 403

    if request.method == "POST":
        problem = Problem(
            title=request.form["title"],
            description=request.form["description"],
            difficulty=request.form["difficulty"],
            marks=int(request.form["marks"]),
            sample_input=request.form.get("sample_input"),
            sample_output=request.form.get("sample_output"),
            input_data=request.form["input_data"],
            expected_output=request.form["expected_output"],
            hidden_input=request.form["hidden_input"],
            hidden_output=request.form["hidden_output"]
        )
        db.session.add(problem)
        db.session.commit()
        return redirect(url_for("admin.manage_problems"))

    problems = Problem.query.all()
    return render_template("admin/manage_problems.html", problems=problems)

# =====================================================
# EDIT PROBLEM
# =====================================================
@admin_bp.route("/admin/problems/edit/<int:pid>", methods=["GET", "POST"])
@login_required
def edit_problem(pid):
    if current_user.role != "admin":
        return "Forbidden", 403

    problem = Problem.query.get_or_404(pid)

    if request.method == "POST":
        problem.title = request.form["title"]
        problem.description = request.form["description"]
        problem.difficulty = request.form["difficulty"]
        problem.marks = int(request.form["marks"])
        problem.sample_input = request.form.get("sample_input")
        problem.sample_output = request.form.get("sample_output")
        problem.input_data = request.form["input_data"]
        problem.expected_output = request.form["expected_output"]
        problem.hidden_input = request.form["hidden_input"]
        problem.hidden_output = request.form["hidden_output"]

        db.session.commit()
        return redirect(url_for("admin.manage_problems"))

    return render_template("admin/edit_problem.html", problem=problem)

# =====================================================
# DELETE PROBLEM
# =====================================================
@admin_bp.route("/admin/problems/delete/<int:pid>")
@login_required
def delete_problem(pid):
    if current_user.role != "admin":
        return "Forbidden", 403

    problem = Problem.query.get_or_404(pid)
    db.session.delete(problem)
    db.session.commit()

    return redirect(url_for("admin.manage_problems"))

# =====================================================
# PROBLEM-WISE SUBMISSION HISTORY
# =====================================================
@admin_bp.route("/admin/problems/history/<int:pid>")
@login_required
def problem_history(pid):
    if current_user.role != "admin":
        return "Forbidden", 403

    problem = Problem.query.get_or_404(pid)

    submissions = (
        db.session.query(Submission, User)
        .join(User, Submission.user_id == User.id)
        .filter(Submission.problem_id == pid)
        .order_by(Submission.submitted_at.desc())
        .all()
    )

    return render_template(
        "admin/problem_history.html",
        problem=problem,
        submissions=submissions
    )

# =====================================================
# VIEW ALL SUBMISSIONS (GLOBAL)
# =====================================================
@admin_bp.route("/admin/submissions")
@login_required
def view_submissions():
    if current_user.role != "admin":
        return "Forbidden", 403

    submissions = (
        db.session.query(Submission, User, Problem)
        .join(User, Submission.user_id == User.id)
        .join(Problem, Submission.problem_id == Problem.id)
        .order_by(Submission.submitted_at.desc())
        .all()
    )

    return render_template(
        "admin/submissions.html",
        submissions=submissions
    )

# =====================================================
# LEADERBOARD (OVERALL)
# =====================================================
@admin_bp.route("/admin/leaderboard")
@login_required
def admin_leaderboard():
    if current_user.role != "admin":
        return "Forbidden", 403

    leaderboard = (
        db.session.query(
            User.username,
            db.func.sum(Submission.score).label("total_score")
        )
        .join(Submission)
        .group_by(User.id)
        .order_by(db.desc("total_score"))
        .all()
    )

    return render_template(
        "admin/leaderboard.html",
        leaderboard=leaderboard
    )

# =====================================================
# ANALYTICS (OVERALL + PROBLEM-WISE)
# =====================================================
@admin_bp.route("/admin/analytics")
@login_required
def admin_analytics():
    if current_user.role != "admin":
        return "Forbidden", 403

    overall = (
        db.session.query(
            User.username,
            db.func.sum(Submission.score).label("total_score")
        )
        .join(Submission)
        .group_by(User.id)
        .order_by(db.desc("total_score"))
        .all()
    )

    problems = Problem.query.all()
    problem_stats = []

    for p in problems:
        results = (
            db.session.query(
                User.username,
                Submission.score
            )
            .join(User, Submission.user_id == User.id)
            .filter(Submission.problem_id == p.id)
            .order_by(Submission.score.desc())
            .all()
        )

        problem_stats.append({
            "problem": p,
            "results": results
        })

    return render_template(
        "admin/analytics.html",
        overall=overall,
        problem_stats=problem_stats
    )

# =====================================================
# DOWNLOAD RESULTS (CSV)
# =====================================================
@admin_bp.route("/admin/download-results")
@login_required
def download_results():
    if current_user.role != "admin":
        return "Forbidden", 403

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "Username",
        "Problem",
        "Status",
        "Score",
        "Submitted At"
    ])

    submissions = (
        db.session.query(Submission, User, Problem)
        .join(User, Submission.user_id == User.id)
        .join(Problem, Submission.problem_id == Problem.id)
        .all()
    )

    for s, u, p in submissions:
        writer.writerow([
            u.username,
            p.title,
            s.status,
            s.score,
            s.submitted_at
        ])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="codemaster_results.csv"
    )