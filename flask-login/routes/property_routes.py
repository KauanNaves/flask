from flask import render_template, Blueprint, redirect, url_for

properties_routes = Blueprint('properties', __name__, url_prefix='/properties')

@properties_routes.route('/dashboard', methods=['GET'])
def home_properties():
    return render_template('dashboard.html')

