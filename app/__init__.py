from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = '123456678'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///baza_danych_zadania.db"

    db.init_app(app)

    from.views import  login_blueprint, logout_blueprint, dashboard_blueprint

    app.register_blueprint(login_blueprint)
    app.register_blueprint(logout_blueprint)
    app.register_blueprint(dashboard_blueprint)

    return app

