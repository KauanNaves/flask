from flask import Blueprint, render_template, redirect, url_for

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return redirect(url_for('students.list_students'))

@main_routes.route('/about')
def about():
    return render_template('about.html')