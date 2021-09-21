from datetime import date

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
        CheckIfRequestIsNotJson(request.is_json)
        json_org_id = request.json.get("org_id")
        CheckIfFieldIsMissing(json_org_id, "org_id")
        # result = GetCompanyFavourites(json_org_id)
        # CheckIfObjectsDoesntExist(result)

        # idList = []
        # for cF in companyFavourites:
        #     idList.append(cF.favourite_org_id)
        # companies = companyResource.GetCompaniesById(idList)
        # for cF in companyFavourites:
        #     for c in companies:
        #         if cF.favourite_org_id == c.org_id:
        #             cFExport = companyFavouritesModel.CompanyFavouriteExport(org_id=c.org_id,
        #                                                                          org_name=c.org_name,
        #                                                                          addition_date=cF.addition_date)
        #             companyFavouritesExport.append(cFExport)
        comps = companyFavouritesModel.CompanyFavourites.get_all()
        print(comps)

        return cFavouriteSchema.dump(comps, many=True)

        return cFavouriteExportSchema.dump(companyFavouritesExport, many=True)

    def post(self):
        CheckIfRequestIsNotJson(request.is_json)
        json_org_id = request.json.get("org_id")
        json_favourite_org_id = request.json.get("favourite_org_id")
        CheckIfFieldIsMissing(json_org_id, "org_id")
        CheckIfFieldIsMissing(json_favourite_org_id, "favourite_org_id")
        cFavouriteModel = companyFavouritesModel.CompanyFavourites(org_id=json_org_id,
                                                                   addition_date=date.today(),
                                                                      favourite_org_id=json_favourite_org_id)
        CheckIfObjectAlreadyExists(FindSpecificFavouriteCompany(json_org_id, json_favourite_org_id))
        companyFavouritesModel.companiesFavourites.append(cFavouriteModel)
        cFavouriteModel.save()

        return cFavouriteSchema.dump(cFavouriteModel)

        return {'msg': 'Company Favourite Added'}, 201

    def put(self):
        return {'msg': 'Request not found'}, 404
    def delete(self):
        CheckIfRequestIsNotJson(request.is_json)
        json_org_id = request.json.get("org_id")
        json_favourite_org_id = request.json.get("favourite_org_id")
        CheckIfFieldIsMissing(json_org_id, "org_id")
        CheckIfFieldIsMissing(json_favourite_org_id, "favourite_org_id")
        result = FindSpecificFavouriteCompany(json_org_id, json_favourite_org_id)
        CheckIfObjectIsNone(result)
        companyFavouritesModel.companiesFavourites.remove(result)

        return {'msg': 'OK'}, 200
