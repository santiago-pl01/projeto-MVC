from flask import Blueprint, render_template

app= Blueprint('app', __name__)

app.route('/')
def home():
    return render_template('index.html')
    