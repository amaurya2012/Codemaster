from flask import Blueprint

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(404)
def not_found(e):
    return "404 Page Not Found", 404

@error_bp.app_errorhandler(403)
def forbidden(e):
    return "403 Forbidden", 403

@error_bp.app_errorhandler(500)
def server_error(e):
    return "500 Internal Server Error", 500
