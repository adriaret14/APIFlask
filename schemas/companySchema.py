from marshmallow import fields, Schema
from flask_marshmallow import Marshmallow


class CompanySchema(Schema):
    org_id = fields.Integer()
    org_name = fields.String()
