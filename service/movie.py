
from dao.movie import MovieDAO, MovieSchema

movie_schema = MovieSchema(many=True)


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_by_director_id(self, director_id):
        return self.dao.get_by_director(director_id)

    def get_by_genre_id(self, genre_id):
        return self.dao.get_by_genre(genre_id)

    def get_by_year(self, year):
        return self.dao.get_by_year_(year)

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):

        movie_id = data.get('id')
        movie = self.get_one(movie_id)
        movie.update(data)

        self.dao.update(movie)

    def delete(self, movie_id):
        return self.dao.delete(movie_id)
