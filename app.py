from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dB import *
from resources import resources



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.register_blueprint(resources.companyBP)
app.register_blueprint(resources.companyFavouritesBP)
db.init_app(app)

ConnectToDatabase()


@app.route('/')
def hello_world():
    return 'Hello World from API!'


if __name__ == '__main__':
    app.run()

