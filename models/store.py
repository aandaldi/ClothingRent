from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id           = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    created_by   = db.Column(db.String(80))
    date_modified= db.Column(db.DateTime)
    modified_by  = db.Column(db.String(80))
    name         = db.Column(db.String(80))
    address      = db.Column(db.String(80))
    owner_name   = db.Column(db.String(80))
    phone        = db.Column(db.String(80))

    def __init__(self,date_created, created_by, date_modified, modified_by, name, address, owner_name, phone):
        self.date_created = date_created
        self.created_by   = created_by
        self.date_modified= date_modified
        self.modified_by  = modified_by
        self.name         = name
        self.address      = address
        self.owner_name   = owner_name
        self.phone        = phone

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()