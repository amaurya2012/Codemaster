from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Problem

# =====================================================
# PROBLEMS BLUEPRINT
# (Must be named problem_bp – used in create_app)
# =====================================================
problem_bp = Blueprint("problem_bp", __name__)

# -----------------------------------------------------
# LIST ALL PROBLEMS
# URL: /problems
# -----------------------------------------------------
@problem_bp.route("/problems")
@login_required
def problems_list():
    problems = Problem.query.order_by(Problem.id.asc()).all()
    return render_template(
        "problems/problems.html",
        problems=problems
    )

# -----------------------------------------------------
# PROBLEM DETAIL + SUBMIT PAGE
# URL: /problems/<id>
# -----------------------------------------------------
@problem_bp.route("/problems/<int:pid>")
@login_required
def problem_detail(pid):
    problem = Problem.query.get_or_404(pid)
    return render_template(
        "problems/problem_detail.html",
        problem=problem
    )
