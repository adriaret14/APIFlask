# from db import db
#
#
# class Company(db.Model):
#     org_id = db.Column(db.Integer, primary_key=True)
#     org_name = db.Column(db.String(100), nullable=False)


companies = []


class Company:
    org_id: int
    org_name: str

    def __init__(self, org_id, org_name):
        self.org_id = org_id
        self.org_name = org_name

