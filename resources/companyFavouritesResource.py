from flask_restful import Resource, request, abort
from error_handler import *
from models import companyFavouritesModel
from resources import companyResource
from schemas import companyFavouritesSchema

cFavouriteSchema = companyFavouritesSchema.CompanyFavouritesSchema()
cFavouriteExportSchema = companyFavouritesSchema.CompanyFavouriteExportSchema()

companyFavourites = []
companyFavouritesExport = []

def DeleteCascadeAllCompanyRegisters(id):
    for cF in companyFavouritesModel.companiesFavourites:
        if cF.org_id == id or cF.favourite_org_id == id:
            companyFavouritesModel.companiesFavourites.remove(cF)

def FindSpecificFavouriteCompany(id, fid):
    searchedFCompany = None
    for cF in companyFavouritesModel.companiesFavourites:
        if cF.org_id == id and cF.favourite_org_id == fid:
            searchedFCompany = cF
    return searchedFCompany

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
        if not request.is_json:
            abort(400, msg='Request body cannot be empty and must be JSON formatted')

        json_org_id = request.json.get("org_id")

        if json_org_id is None:
            abort(400, msg='Missing required field org_id')

        result = GetCompanyFavourites(json_org_id)

        if result:
            idList = []
            for cF in companyFavourites:
                idList.append(cF.favourite_org_id)

            companies = companyResource.GetCompaniesById(idList)
            for cF in companyFavourites:
                for c in companies:
                    if cF.favourite_org_id == c.org_id:
                        cFExport = companyFavouritesModel.CompanyFavouriteExport(org_id=c.org_id,
                                                                                 org_name=c.org_name,
                                                                                 addition_date=cF.addition_date)
                        companyFavouritesExport.append(cFExport)

            return cFavouriteExportSchema.dump(companyFavouritesExport, many=True)
        else:
            abort(404, msg='Company not found')

    def post(self):
        if not request.is_json:
            abort(400, msg='Request body cannot be empty and must be JSON formatted')

        json_org_id = request.json.get("org_id")
        json_favourite_org_id = request.json.get("favourite_org_id")

        if json_org_id is None:
            abort(400, msg='Missing required field org_id')

        if json_favourite_org_id is None:
            abort(400, msg='Missing required field favourite_org_id')

        cFavouriteModel = companyFavouritesModel.CompanyFavourites(org_id=json_org_id,
                                                                   favourite_org_id=json_favourite_org_id)

        if (FindSpecificFavouriteCompany(json_org_id, json_favourite_org_id)) is None:
            companyFavouritesModel.companiesFavourites.append(cFavouriteModel)
        else:
            abort(400, msg='The favourited company already exists')

        return {'msg': 'Company Favourite Added'}, 201

    def put(self):
        return {'msg': 'Request not found'}, 404
    def delete(self):
        if not request.is_json:
            abort(400, msg='Request body cannot be empty and must be JSON formatted')

        json_org_id = request.json.get("org_id")
        json_favourite_org_id = request.json.get("favourite_org_id")

        if json_org_id is None:
            abort(400, msg='Missing required field org_id')

        if json_favourite_org_id is None:
            abort(400, msg='Missing required field favourite_org_id')

        result = FindSpecificFavouriteCompany(json_org_id, json_favourite_org_id)
        if result is not None:
            companyFavouritesModel.companiesFavourites.remove(result)
        else:
            abort(404, msg='Company not found')

        return {'msg': 'OK'}, 200
