
from setup_db import db
from marshmallow import Schema, fields


class GenreModel(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


