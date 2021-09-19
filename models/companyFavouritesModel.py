from datetime import date

from db import db

# class CompanyFavourites(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     org_id = db.Column(db.Integer)
#     favourite_org_id = db.Column(db.Integer)


companiesFavourites = []


class CompanyFavourites:
    org_id: int
    #addition_date: date
    favourite_org_id: int

    def __init__(self, org_id, favourite_org_id):
        self.org_id = org_id
        #self.addition_date = date.today()
        self.favourite_org_id = favourite_org_id

