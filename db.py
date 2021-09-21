import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def ConnectToDatabase():
    connection = sqlite3.connect('database.db')

    cursor= connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Company(org_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        org_name TEXT NOT NULL)''')
    connection.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS CompanyFavourites(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            org_id TEXT NOT NULL,
                                                            addition_date TEXT NOT NULL,
                                                            favourite_org_id INTEGER,
                                                            FOREIGN KEY(org_id) REFERENCES Company(org_id),
                                                            FOREIGN KEY(favourite_org_id) REFERENCES Company(org_id))''')

    connection.commit()

class BaseModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()



