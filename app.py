
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from flask import Flask
from controllers.auth.login import login
from controllers.dashboard.dashboard import dashboard
from controllers.notas.notas import notas
from utils.config import config
from utils.db import db
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    app.secret_key = "3ntr4r1234$"
    app.permanent_session_lifetime = timedelta(minutes=60)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(login)
    app.register_blueprint(dashboard)
    app.register_blueprint(notas)
    return app




if __name__ == "__main__":
    app = create_app()
    app.run()

    