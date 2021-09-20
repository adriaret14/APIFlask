from flask_restful import Resource, request
from error_handler import *
from models import companyFavouritesModel
from resources import companyResource
from schemas import companyFavouritesSchema

cFavouriteSchema = companyFavouritesSchema.CompanyFavouritesSchema()
cFavouriteExportSchema = companyFavouritesSchema.CompanyFavouriteExportSchema()

companyFavourites = []
companyFavouritesExport = []


def GetCompanyFavourites(id):
    companyFound = False
    ClearCompanyFavouritesLists()

    for cF in companyFavouritesModel.companiesFavourites:
        if cF.org_id  == id:
            companyFound=True
            companyFavourites.append(cF)
    return companyFound


def ClearCompanyFavouritesLists():
    companyFavourites.clear()
    companyFavouritesExport.clear()


class CompanyFavourites(Resource):
    def get(self):
        data = request.get_json()
        if data != None:
            companyFavourites_dict = cFavouriteSchema.load(data)
        else:
            raise RequestBodyEmpty('Request body cannot be empty and must be JSON formatted')

        result = GetCompanyFavourites(companyFavourites_dict['org_id'])

        if result == True:
            idList = []
            for cF in companyFavourites:
                idList.append(cF.favourite_org_id)

            companies = companyResource.GetCompaniesById(idList)
            for cF in companyFavourites:
                for c in companies:
                    if cF.favourite_org_id == c.org_id:
                        cFExport = companyFavouritesModel.CompanyFavouriteExport(org_id = c.org_id,
                                                                      org_name = c.org_name,
                                                                      addition_date = cF.addition_date)
                        companyFavouritesExport.append(cFExport)

            return cFavouriteExportSchema.dump(companyFavouritesExport, many=True)
        else:
            raise ObjectNotFound('Company not found')

    def post(self):
        data = request.get_json()
        companyFavourites_dict = cFavouriteSchema.load(data)
        cFavouriteModel = companyFavouritesModel.CompanyFavourites(org_id = companyFavourites_dict['org_id'],
                                                                   favourite_org_id = companyFavourites_dict['favourite_org_id'])
        companyFavouritesModel.companiesFavourites.append(cFavouriteModel)
        return {"data": "CompanyFavourites POST request"}
    def put(self):
        return {"data": "CompanyFavourites PUT request"}
    def delete(self):
        return {"data": "CompanyFavourites DELETE request"}
