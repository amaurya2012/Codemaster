from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app.models import Submission, Problem
from app.extensions import db
from app.utils.evaluator import evaluate

# =====================================================
# SUBMISSIONS BLUEPRINT
# =====================================================
submission_bp = Blueprint("submissions", __name__)

@submission_bp.route("/submit/<int:pid>", methods=["GET", "POST"])
@login_required
def submit(pid):
    problem = Problem.query.get_or_404(pid)

    if request.method == "POST":
        # -------------------------------
        # READ FORM DATA
        # -------------------------------
        code = request.form["code"]
        language = request.form.get("language", "python")

        # =================================================
        # PUBLIC TEST CASES (DETAILS SHOWN)
        # =================================================
        public_inputs = problem.input_data.splitlines()
        public_outputs = problem.expected_output.splitlines()

        status_pub, percent_pub, details = evaluate(
            code,
            language,
            public_inputs,
            public_outputs
        )

        # =================================================
        # HIDDEN TEST CASES (NO DETAILS)
        # =================================================
        hidden_inputs = problem.hidden_input.splitlines()
        hidden_outputs = problem.hidden_output.splitlines()

        status_hid, percent_hid, _ = evaluate(
            code,
            language,
            hidden_inputs,
            hidden_outputs
        )

        # =================================================
        # FINAL STATUS & SCORE LOGIC
        # =================================================
        if status_pub == "Accepted" and status_hid == "Accepted":
            final_status = "Accepted"
            final_percent = 100

        elif status_pub in [
            "Compilation Error",
            "Runtime Error",
            "Time Limit Exceeded",
            "Memory Limit Exceeded"
        ]:
            final_status = status_pub
            final_percent = 0

        else:
            final_status = "Wrong Answer"
            final_percent = int((percent_pub + percent_hid) / 2)

        final_score = int((final_percent / 100) * problem.marks)

        # =================================================
        # SAVE SUBMISSION
        # =================================================
        submission = Submission(
            code=code,
            language=language,
            status=final_status,
            score=final_score,
            user_id=current_user.id,
            problem_id=pid
        )

        db.session.add(submission)
        db.session.commit()

        # =================================================
        # SHOW RESULT PAGE
        # =================================================
        return render_template(
            "submissions/result.html",
            status=final_status,
            score=final_score,
            total_marks=problem.marks,
            details=details
        )

    # -------------------------------
    # GET REQUEST → SHOW SUBMIT PAGE
    # -------------------------------
    return render_template(
        "submissions/submit.html",
        problem=problem
    )
