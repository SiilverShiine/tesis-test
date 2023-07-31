from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

# TODO: Refactor and move content to app.py

app = Flask(__name__)

# Connection to DB
# TODO: Change password, use env var
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/documentsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

contacts = Blueprint('contacts', __name__)


@contacts.route('/db')
def home_db():
    return "it's working"


if __name__ == "__main__":
    app.run(debug=True)
