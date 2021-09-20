from datetime import date

from db import db

# class CompanyFavourites(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     org_id = db.Column(db.Integer)
#     favourite_org_id = db.Column(db.Integer)


companiesFavourites = []


class CompanyFavourites:
    org_id: int
    addition_date: date
    favourite_org_id: int

    def __init__(self, org_id, favourite_org_id):
        self.org_id = org_id
        self.addition_date = date.today()
        self.favourite_org_id = favourite_org_id


class CompanyFavouriteExport:
    org_id: int
    org_name: str
    addition_date: date

    def __init__(self, org_id, org_name, addition_date):
        self.org_id = org_id
        self.org_name = org_name
        self.addition_date = addition_date
