from flask import Flask
from views import app as views_app

app = Flask(__name__)
app.register_blueprint(views_app)

if __name__ == '__main__':
    app.run(debug=True)
