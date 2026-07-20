from flask_login import current_user
from functools import wraps

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.role != "admin":
            return "Unauthorized"
        return f(*args, **kwargs)
    return wrap
