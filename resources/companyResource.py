import flask
from flask_restful import Resource, request, reqparse, abort

from error_handler import *
from models import companyModel
from schemas import companySchema


cSchema = companySchema.CompanySchema()

#Only use if using API with variables
companyIdCont = 0

def CheckCompanyDoesntExist(name):
    for c in companyModel.companies:
        if c.org_name == name:
            return True

    return False

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


class Company(Resource):
    def get(self):
        if not request.is_json:
            abort(400, msg='Request body cannot be empty and must be JSON formatted')

        json_org_id = request.json.get("org_id")

        if json_org_id is None:
            abort(400, msg='Missing required field org_id')

        result = GetCompanyById(json_org_id)

        if result is not None:
            return cSchema.dump(GetCompanyById(json_org_id)), 200
        else:
            abort(404, msg='Company not found')

    def post(self):
        global companyIdCont

        if not request.is_json:
            abort(400, msg='Request body cannot be empty and must be JSON formatted')

        json_org_name = request.json.get("org_name")

        if json_org_name is None:
            abort(400, msg='Missing required field org_name')

        if CheckCompanyDoesntExist(json_org_name) == False:
            cModel = companyModel.Company(org_id=companyIdCont,
                                         org_name=json_org_name)
        else:
            abort(400, msg='The company already exists')

        companyIdCont += 1
        companyModel.companies.append(cModel)
        return {'msg': 'Company created'}, 201

    def put(self):
        if not request.is_json:
            abort(400, msg='Request body cannot be empty and must be JSON formatted')

        json_org_id = request.json.get("org_id")
        json_org_name = request.json.get("org_name")

        if json_org_id is None:
            abort(400, msg='Missing required field org_id')

        if json_org_name is None:
            abort(400, msg='Missing required field org_name')

        updCompany = GetCompanyById(json_org_id)
        if updCompany != None:
            updCompany.org_name = json_org_name
        else:
            abort(404, msg='Company not found')

        return {'msg': 'OK'}, 200

    def delete(self):   #Need to take in mind the delCompany in favourites and remove them also
        if not request.is_json:
            abort(400, msg='Request body cannot be empty and must be JSON formatted')

        json_org_id = request.json.get("org_id")

        if json_org_id is None:
            abort(400, msg='Missing required field org_id')

        delCompany = GetCompanyById(json_org_id)
        if delCompany != None:
            companyModel.companies.remove(delCompany)
        else:
            abort(404, msg='Company not found')

        return {'msg': 'OK'}, 200

