from RCcars import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    position = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, name, number):
        self.username = name
        self.number = number

    def __repr__(self):
        return f"{self.id}: {self.username}, {self.number}, {self.position}"
