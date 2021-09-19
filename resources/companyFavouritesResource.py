from datetime import date

from flask_restful import Resource, request
from models import companyFavouritesModel
from schemas import companyFavouritesSchema

cFavouriteSchema = companyFavouritesSchema.CompanyFavouritesSchema()
companyFavourites = []


def GetCompanyFavourites(id):
    companyFound = False
    ClearCompanyFavourites()

    for cF in companyFavouritesModel.companiesFavourites:
        if cF.org_id  == id:
            companyFound=True
            companyFavourites.append(cF)
    return companyFound


def ClearCompanyFavourites():
    companyFavourites.clear()


class CompanyFavourites(Resource):
    def get(self):
        data = request.get_json()
        if data != None:
            companyFavourites_dict = cFavouriteSchema.load(data)
        else:
            return {"data": "GET Request body was empty"}

        result = GetCompanyFavourites(companyFavourites_dict['org_id'])

        if result == True:
            print(companyFavourites)
            return cFavouriteSchema.dump(companyFavourites, many=True)  #Need to dump company Information, not CompanyFavourites Table
        else:
            return {"data": "Company not found, Invalid data"}

    def post(self):
        data = request.get_json()
        companyFavourites_dict = cFavouriteSchema.load(data)
        cFavouriteModel = companyFavouritesModel.CompanyFavourites(org_id = companyFavourites_dict['org_id'],
                                                                   favourite_org_id = companyFavourites_dict['favourite_org_id']) #Need to add additon_date
        companyFavouritesModel.companiesFavourites.append(cFavouriteModel)
        return {"data": "CompanyFavourites POST request"}
    def put(self):
        return {"data": "CompanyFavourites PUT request"}
    def delete(self):
        return {"data": "CompanyFavourites DELETE request"}
