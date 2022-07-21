from dao.model.director import DirectorModel
from flask import json


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(DirectorModel).all()

    def create(self, data):
        director = DirectorModel(**data)

        self.session.add(director)
        self.session.commit()

        return director

    def get_one(self, director_id):
        return self.session.query(DirectorModel).filter(DirectorModel.id == director_id)

    def update(self, director):
        self.session.commit()

        return director

    def delete(self, director_id):
        director = self.session.query(DirectorModel).get(director_id)

        self.session.delete(director)
        self.session.commit()
