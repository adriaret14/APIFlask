from flask_restful import Resource, request

from error_handler import *
from models import companyModel
from schemas import companySchema


cSchema = companySchema.CompanySchema()

#Only use if using API with variables
companyIdCont = 0


def CheckCompanyDoesntExist(name):
    for c in companyModel.companies:
        print(c.org_name)


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
        data = request.get_json()
        if data != None:
            company_dict = cSchema.load(data)
        else:
            raise RequestBodyEmpty('Request body cannot be empty and must be JSON formatted')

        result = GetCompanyById(company_dict['org_id'])

        if result != None:
            return cSchema.dump(GetCompanyById(company_dict['org_id'])), 200
        else:
            raise ObjectNotFound('Company not found')

    def post(self):
        global companyIdCont

        data = request.get_json()
        company_dict = cSchema.load(data)
        cModel = companyModel.Company(org_id = companyIdCont,
                                      org_name=company_dict['org_name'])
        companyIdCont += 1
        companyModel.companies.append(cModel)
        return {"data": "Company POST request"}

    def put(self):
        print(request.get_json())
        return {"data": "Company PUT request"}

    def delete(self):
        print(request.get_json())
        return {"data": "Company DELETE request"}
