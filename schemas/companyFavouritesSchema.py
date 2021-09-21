from marshmallow import fields
from flask_marshmallow import Marshmallow, Schema


class CompanyFavouritesSchema(Schema):
    org_id = fields.Integer(dump_only=True)
    addition_date = fields.Date()
    favourite_org_id = fields.Integer()


class CompanyFavouriteExportSchema(Schema):
    org_id = fields.Integer()
    org_name = fields.String()
    addition_date = fields.Date()
