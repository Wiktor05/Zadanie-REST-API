from flask import Blueprint, request, session, flash, render_template, redirect, url_for
from .models import Users
from . import db


login_blueprint = Blueprint("login", __name__)
dashboard_blueprint = Blueprint("dashboard", __name__)
logout_blueprint = Blueprint("logout", __name__)


@login_blueprint.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        nickname = request.form["nickname"]
        found_user = Users.query.filter_by(name=nickname).first()

        if not found_user:
            new_user = Users(name=nickname, email=None)
            db.session.add(new_user)
            db.session.commit()
            session.update({"nick" : nickname, "email" : None})

            flash("You have been successfully registered.", "success")
        else:
            session.update({"nick" : nickname, "email" : found_user_email})
            flash("you have been successfully logged in.", "success")
    elif request.method == "GET" and "nick" not in session:
        return render_template("login.html")
    elif request.method == "GET" and "nick" in session:
         flash("Already logged in", "warning")

    return redirect(url_for("dashboard.dashboard"))


@logout_blueprint.route('/logout')
def logout():
    if "nick" in session:
        session.pop("nick", None)
        session.pop("email", None)
        flash("You have been logged out", "success")
    else:
        flash("You are not logged in ", "warning")
    return redirect(url_for("login.login"))

@dashboard_blueprint.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    if "nick" in session:
        nickname = session["nick"]
        email = session["email"]

        if request.method == "POST":
            found_user = Users.query.filter_by(name=nickname).first()
            email = request.form["email"]
            found_user.email = email
            db.session.commit()
            session.update({"email" : email})

        return render_template("dashboard.html", nickname=nickname, email=email)

    else:
        flash("You are not logged in", "warning")

    return redirect(url_for("login.login"))



