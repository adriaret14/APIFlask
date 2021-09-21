from flask import Flask, jsonify
from error_handler import *
from resources import resources

app = Flask(__name__)
app.register_blueprint(resources.companyBP)
app.register_blueprint(resources.companyFavouritesBP)



@app.route('/')
def hello_world():
    return 'Hello World from API!'


if __name__ == '__main__':
    app.run(Debug=False)

