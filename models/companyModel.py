from dB import db, BaseModelMixin


class Company(db.Model, BaseModelMixin):
    org_id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(100), nullable=False)
    # org_favourite_owner = db.relationship('CompanyFavourites', backref='org_id')
    # org_favourite_usage = db.relationship('CompanyFavourites', backref='favourite_org_id')


companies = []


class CompanyMod:
    org_id: int
    org_name: str

    def __init__(self, org_id, org_name):
        self.org_id = org_id
        self.org_name = org_name

