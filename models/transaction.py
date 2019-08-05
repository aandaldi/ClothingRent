from db import db

class TransactionModel(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)    date_created = db.Column(db.DateTime)
    created_by = db.Column(db.String(80))
    date_modified = db.Column(db.DateTime)
    modified_by = db.Column(db.String(80))
    product_uuid= db.Column(db.Integer, db.ForeignKey('products.id'))
    owner_uuid = db.Column(db.Integer, db.ForeignKey('users.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    total_price = db.Column(db.String(25))

    product = db.relationship('ProductModel')
    user = db.relationship('UserModel')

    def __init__(self, date_created, created_by, date_modified, modified_by, product_id, owner_id, start_date, end_date,total_price):
        self.date_created = date_created
        self.created_by = created_by
        self.date_modified = date_modified
        self.modified_by = modified_by
        self.product_id = product_id
        self.owner_id = owner_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price

    def json(self):
        # return {'date_created' :  self.date_created.strftime("%Y-%m-%d %H:%M:%S:%f"), 'created_by' :  self.created_by,'date_modified' :  self.date_modified, 'modified_by' :  self.modified_by,
        #    'product_id' :  self.product_id, 'owner_id' :  self.owner_id, 'start_date' :  self.start_date, 'end_date' :  self.end_date, 'total_price' :  self.total_price }
        return "oke"

    @classmethod
    def find_by_name(cls, _id):
        return cls.query.filter_by(id=_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    