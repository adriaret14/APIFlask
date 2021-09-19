from flask_restful import Resource, request
from models import companyModel
from schemas import companySchema


cSchema = companySchema.CompanySchema()


def CompanyVerification(name):
    for c in companyModel.companies:
        print(c.org_name)


def GetCompanyById(id):
    foundCompany=None
    for c in companyModel.companies:
        if c.org_id == id:
            foundCompany=c
            break
    return foundCompany


class Company(Resource):
    def get(self):
        print(request.get_json())
        data = request.get_json()
        company_dict = cSchema.load(data)

        result = GetCompanyById(company_dict['org_id'])

        if result != None:
            return cSchema.dumps(GetCompanyById(company_dict['org_id']))
        else:
            return {"data": "Company not found"}
    def post(self):

        data = request.get_json()
        #print(data)
        company_dict = cSchema.load(data)
        #print(company_dict)
        cModel = companyModel.Company(org_id=company_dict['org_id'],
                                      org_name=company_dict['org_name'])
        companyModel.companies.append(cModel)
        #print(companyModel.companies)
        return {"data": "Company POST request"}
    def put(self):
        print(request.get_json())
        return {"data": "Company PUT request"}
    def delete(self):
        print(request.get_json())
        return {"data": "Company DELETE request"}