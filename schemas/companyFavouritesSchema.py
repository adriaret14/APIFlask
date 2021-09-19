from marshmallow import fields, Schema
from flask_marshmallow import Marshmallow


class CompanyFavouritesSchema(Schema):
    org_id = fields.Integer()
    #addition_date = fields.Date()
    favourite_org_id = fields.Integer()
