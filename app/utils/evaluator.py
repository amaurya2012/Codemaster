import subprocess
import tempfile
import os
import shutil

# -------------------------------
# CONFIGURATION
# -------------------------------
TIME_LIMIT = 2        # seconds
MAX_CODE_SIZE = 10000 # characters


# -------------------------------
# OUTPUT NORMALIZATION
# -------------------------------
def normalize(text):
    return text.strip().replace("\r\n", "\n").strip()


# -------------------------------
# MAIN EVALUATOR FUNCTION
# -------------------------------
def evaluate(code, language, inputs, outputs):
    """
    Returns:
    status, percentage, details
    """

    if len(code) > MAX_CODE_SIZE:
        return "Memory Limit Exceeded", 0, []

    passed = 0
    total = len(inputs)
    details = []

    workdir = tempfile.mkdtemp()

    try:
        # -------------------------------
        # SETUP BASED ON LANGUAGE
        # -------------------------------
        if language == "python":
            src = os.path.join(workdir, "solution.py")
            with open(src, "w", encoding="utf-8") as f:
                f.write(code)
            run_cmd = ["python", src]

        elif language == "c":
            src = os.path.join(workdir, "solution.c")
            exe = os.path.join(workdir, "solution.exe")
            with open(src, "w", encoding="utf-8") as f:
                f.write(code)

            compile_proc = subprocess.run(
                ["gcc", src, "-o", exe],
                capture_output=True,
                text=True
            )
            if compile_proc.returncode != 0:
                return "Compilation Error", 0, [compile_proc.stderr]

            run_cmd = [exe]

        elif language == "java":
            src = os.path.join(workdir, "Main.java")
            with open(src, "w", encoding="utf-8") as f:
                f.write(code)

            compile_proc = subprocess.run(
                ["javac", src],
                cwd=workdir,
                capture_output=True,
                text=True
            )
            if compile_proc.returncode != 0:
                return "Compilation Error", 0, [compile_proc.stderr]

            run_cmd = ["java", "-cp", workdir, "Main"]

        else:
            return "Unsupported Language", 0, []

        # -------------------------------
        # EXECUTE TEST CASES (PUBLIC ONLY)
        # -------------------------------
        for i in range(total):
            try:
                proc = subprocess.run(
                    run_cmd,
                    input=inputs[i],
                    text=True,
                    capture_output=True,
                    timeout=TIME_LIMIT
                )

                user_out = normalize(proc.stdout)
                exp_out = normalize(outputs[i])

                if user_out == exp_out:
                    passed += 1
                    result = "Passed"
                else:
                    result = "Failed"

                details.append({
                    "input": inputs[i],
                    "expected": exp_out,
                    "output": user_out,
                    "result": result
                })

            except subprocess.TimeoutExpired:
                return "Time Limit Exceeded", 0, []
            except Exception:
                return "Runtime Error", 0, []

        percent = int((passed / total) * 100)

        if passed == total:
            return "Accepted", 100, details
        else:
            return "Wrong Answer", percent, details

    finally:
        shutil.rmtree(workdir, ignore_errors=True)
