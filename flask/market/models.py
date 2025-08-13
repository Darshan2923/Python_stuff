from market import app, db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False,unique=True)
    barcode = db.Column(db.String(length=12), unique=True, nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description=db.Column(db.String(length=100), nullable=False,unique=True)

    def __repr__(self):
        return f"Item('{self.name}', '{self.barcode}', '{self.price}')"

