from app import create_app
from app import db
import os


def create_db():
    with app.app_context():
        if not os.path.exists("baza_danych_zadania.db"):
            db.create_all()

if __name__ == "__main__":
    app = create_app()
    create_db()
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
