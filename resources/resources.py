from flask import Blueprint
from flask_restful import Api
from resources.companyResource import Company

companyBP = Blueprint('Company', __name__)

api = Api(companyBP)

api.add_resource(Company, "/Company")
