from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to the Volunteer Platform!"
