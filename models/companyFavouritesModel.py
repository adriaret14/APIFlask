from db import db

class CompanyFavourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    org_id = db.Column(db.Integer)