from flask_restful import Resource, request

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
        if(data != None):
            company_dict = cSchema.load(data)
        else:
            raise RequestBodyEmpty('Request body cannot be empty and must be JSON formatted')

        if CheckCompanyDoesntExist(company_dict['org_name']) == False:
            cModel = companyModel.Company(org_id = companyIdCont,
                                         org_name=company_dict['org_name'])
        else:
            raise ObjectAlreadyExists('This company already exists')

        companyIdCont += 1
        companyModel.companies.append(cModel)
        return {'msg': 'Company created'}, 201

    def put(self):
        data = request.get_json()
        if (data != None):
            company_dict = cSchema.load(data)
        else:
            raise RequestBodyEmpty('Request body cannot be empty and must be JSON formatted')

        updCompany = GetCompanyById(company_dict['org_id'])
        if updCompany != None:      #Need to take in mind what happens if not all params have been sent
            updCompany.org_name = company_dict['org_name']
        else:
            raise ObjectNotFound('Company not found')

        return {'msg': 'OK'}, 200

    def delete(self):   #Need to take in mind the delCompany in favourites and remove them also
       data = request.get_json()
       if(data != None):
           company_dict = cSchema.load(data)
       else:
           raise RequestBodyEmpty('Request body cannot be empty and must be JSON formatted')

       delCompany = GetCompanyById(company_dict['org_id'])
       if delCompany != None:
            companyModel.companies.remove(delCompany)
       else:
           raise ObjectNotFound('Company not found')

       return {'msg': 'OK'}, 200
