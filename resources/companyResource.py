import flask
from flask_restful import Resource, request, reqparse, abort

from error_handler import *
from models import companyModel
from resources import companyFavouritesResource
from schemas import companySchema


cSchema = companySchema.CompanySchema()

#Only use if using API with variables
companyIdCont = 0


def GetCompaniesById(idList):
    companiesData = []
    cont = 0
    while cont < len(idList):
        for c in companyModel.companies:
            if c.org_id == idList[cont]:
                companiesData.append(c)
                break
        cont += 1
    return companiesData

def GetCompanyById(id):
    foundCompany=None
    for c in companyModel.companies:
        if c.org_id == id:
            foundCompany=c
            break
    return foundCompany

def GetCompanyByName(name):
    foundCompany = None
    for c in companyModel.companies:
        if c.org_name == name:
            foundCompany=c
            break
    return foundCompany


class Company(Resource):
    def get(self):
        CheckIfRequestIsNotJson(request.is_json)
        json_org_id = request.json.get("org_id")
        CheckIfFieldIsMissing(json_org_id, "org_id")
        result = GetCompanyById(json_org_id)
        CheckIfObjectIsNone(result)

        return cSchema.dump(result), 200

    def post(self):
        global companyIdCont

        CheckIfRequestIsNotJson(request.is_json)
        json_org_name = request.json.get("org_name")
        CheckIfFieldIsMissing(json_org_name, "org_name")
        CheckIfObjectAlreadyExists(GetCompanyByName(json_org_name))
        # cModel = companyModel.CompanyMod(org_id=companyIdCont,
        #                                  org_name=json_org_name)
        cModel = companyModel.Company(org_name=json_org_name)
        #companyIdCont += 1
        companyModel.companies.append(cModel)
        cModel.save()
        #companySchema.dump(cModel)

        return {'msg': 'Company created'}, 201

    def put(self):
        CheckIfRequestIsNotJson(request.is_json)
        json_org_id = request.json.get("org_id")
        json_org_name = request.json.get("org_name")
        CheckIfFieldIsMissing(json_org_id, "org_id")
        CheckIfFieldIsMissing(json_org_name, "org_name")
        updCompany = GetCompanyById(json_org_id)
        CheckIfObjectIsNone(updCompany)
        updCompany.org_name = json_org_name

        return {'msg': 'OK'}, 200

    def delete(self):
        CheckIfRequestIsNotJson(request.is_json)
        json_org_id = request.json.get("org_id")
        CheckIfFieldIsMissing(json_org_id, "org_id")
        delCompany = GetCompanyById(json_org_id)
        CheckIfObjectIsNone(delCompany)
        companyModel.companies.remove(delCompany)
        companyFavouritesResource.DeleteCascadeAllCompanyRegisters(json_org_id)

        return {'msg': 'OK'}, 200

