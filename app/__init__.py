from flask import Flask
from config import Config
from .extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .auth.routes import auth_bp
    from .user.routes import user_bp
    from .admin.routes import admin_bp
    from .problems.routes import problem_bp
    from .submissions.routes import submission_bp
    from .leaderboard.routes import leaderboard_bp
    from .errors.handlers import error_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(problem_bp)
    app.register_blueprint(submission_bp)
    app.register_blueprint(leaderboard_bp)
    app.register_blueprint(error_bp)

    with app.app_context():
        db.create_all()

    return app
