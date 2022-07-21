
from dao.model.movie import MovieModel, MovieSchema

movie_schema = MovieSchema(many=True)  # создание экземпляра схемы


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(MovieModel).all()

    def create(self, data):
        movie = MovieModel(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def get_one(self, movie_id):
        return self.session.query(MovieModel).filter(MovieModel.id == movie_id)

    def get_by_director(self, director_id):
        result = self.session.query(MovieModel).filter(MovieModel.director_id == director_id)
        return movie_schema.dump(result), 200

    def get_by_genre(self, genre_id):
        result = self.session.query(MovieModel).filter(MovieModel.genre_id == genre_id)
        return movie_schema.dump(result), 200

    def get_by_year_(self, year):
        result = self.session.query(MovieModel).filter(MovieModel.year == year)
        return movie_schema.dump(result), 200

    def update(self, movie):
        self.session.commit()

        return movie

    def delete(self, movie_id):
        movie = self.session.query(MovieModel).get(movie_id)

        self.session.delete(movie)
        self.session.commit()
