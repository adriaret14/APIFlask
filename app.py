from flask import Flask
from resources import resources

app = Flask(__name__)
app.register_blueprint(resources.companyBP)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from API!'


if __name__ == '__main__':
    app.run(Debug=True)


#curl -v http://127.0.0.1:5000/FavouriteCompanies

#curl -X POST -H "Content-Type: application/json" \ -d '{"id": 0,"favourite_org_ids: [1, 2, 3]"}' \ http://127.0.0.1:5000/FavouriteCompanies

#curl -d @request.json -H "Content-Type: application/json" http://127.0.0.1:5000/FavouriteCompanies
#curl -d @request.json -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/FavouriteCompanies
#curl -X DELETE http://127.0.0.1:5000/FavouriteCompanies