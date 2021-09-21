from marshmallow import fields
from flask_marshmallow import Marshmallow, Schema


class CompanySchema(Schema):
    org_id = fields.Integer()
    org_name = fields.String()
    org_favourite_owner = fields.Nested('CompanyFavourites', many=True)
    org_favourite_usage = fields.Nested('CompanyFavourites', many=True)
