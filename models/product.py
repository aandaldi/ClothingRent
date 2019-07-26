from db import db

class ProductModel(db.Model):
    __tablename__ = "products"

    id           = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    created_by   = db.Column(db.String(80))
    date_modified= db.Column(db.DateTime)
    modified_by  = db.Column(db.String(80))
    name         = db.Column(db.String(80))
    type         = db.Column(db.String(80))
    color        = db.Column(db.String(80))
    size         = db.Column(db.String(80))
    details      = db.Column(db.String(80))
    price        = db.Column(db.Float(precision=2))
    store_id     = db.Column(db.Integer, db.ForeignKey('stores.id'))
    
    
    store = db.relationship('StoreModel')
    transaction = db.relationship('TransactionModel', lazy='dynamic')


    def __init__(self, date_created, created_by, date_modified, modified_by, name, type,
        color, size, details, price, store_id):
        
        self.date_created = date_created
        self.created_by = created_by
        self.date_modified = date_modified
        self.modified_by = modified_by
        self.name = name
        self.type = type
        self.color = color
        self.size = size
        self.details = details
        self.price = price
        self.store_id = store_id

    
    def json(self):
        return {'name':self.name, 'type':self.type, 'color':self.color, 'size':self.size, 'details':self.details,
            'price':self.price, 'store_id':self.store_id}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()