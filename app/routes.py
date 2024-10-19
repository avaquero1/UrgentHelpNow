from flask import Blueprint, render_template

# Define the blueprint for the main routes
main = Blueprint('main', __name__)

# Route for the home/landing page
@main.route('/')
def index():
    return render_template('index.html')
