from dao.model.genre import GenreModel


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(GenreModel).all()

    def create(self, data):
        genre = GenreModel(**data)

        self.session.add(genre)
        self.session.commit()

        return genre

    def get_one(self, genre_id):
        return self.session.query(GenreModel).filter(GenreModel.id == genre_id)

    def update(self, genre):

        self.session.commit()


    def delete(self, genre_id):
        genre = self.session.query(GenreModel).get(genre_id)

        self.session.delete(genre)
        self.session.commit()

