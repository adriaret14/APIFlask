from flask import Blueprint
from flask_restful import Api

from resources.companyFavouritesResource import CompanyFavourites
from resources.companyResource import Company

companyBP = Blueprint('Company', __name__)
companyFavouritesBP = Blueprint('CompanyFavourites', __name__)

api = Api(companyBP)
api = Api(companyFavouritesBP)

api.add_resource(Company, "/Company")
api.add_resource(CompanyFavourites, "/CompanyFavourites")
