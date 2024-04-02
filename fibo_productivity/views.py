# will house all routes related to our core blog applications (blog, create a blog, user profiles, etc)

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Goals
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/productivity")
@login_required
def fibonacci_productivity():
    return render_template("productivity.html", user=current_user)


@views.route("/manage_goals")
@login_required
def manage_goals():
    return render_template("manage_goals.html", user=current_user)


@views.route("/create-goals", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')

        if not text:
            flash('Goal cannot be empty', category='error')
        else:
            goals = Goals(text=text, author=current_user.id)
            db.session.add(goals)
            db.session.commit()
            flash('Goal created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_goals.html', user=current_user)