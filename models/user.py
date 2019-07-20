from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    # Table Column
    id           = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    created_by   = db.Column(db.String(80))
    date_modified= db.Column(db.DateTime)
    modified_by  = db.Column(db.String(80))
    full_name    = db.Column(db.String(80))
    gender       = db.Column(db.String(80))
    phone        = db.Column(db.String(80))
    address      = db.Column(db.String(80))
    email        = db.Column(db.String(80))
    password     = db.Column(db.String(80))

    def __init__(self, date_created, created_by, date_modified, modified_by, full_name, gender, phone, address, email, password):
        self.date_created = date_created
        self.created_by = created_by
        self.date_modified = date_modified
        self.modified_by = modified_by
        self.full_name = full_name
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email
        self.password = password

    # JSON              ==>> to give data with json format
    def json(self):
        return {'full_name':self.full_name, 'gender':self.gender, 'phone':self.phone,
            'address': self.address, 'email' : self.email}

    @classmethod
    def find_by_name(cls, full_name):
        return cls.query.filter_by(full_name = full_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # def update_db(self, name):
    #     db.session.

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()     
        


