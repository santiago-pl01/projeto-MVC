from flask import Flask
from app.views import app as views_app

app = Flask(__name__)
app.register_blueprint(views_app)

if __name__ == '__main':
    app.run(debug=True)
