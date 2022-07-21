from flask_restx import Resource, Namespace
from dao.model.movie import MovieModel, MovieSchema
from flask import request
from container import movie_service

movie_schema = MovieSchema(many=True)
movie_ns = Namespace("movies")


@movie_ns.route("/")
@movie_ns.param("director_id", "id Режиссера")
@movie_ns.param("genre_id", "id жанра")
@movie_ns.param("year", "год")
class MoviesView(Resource):
    def get(self):
        """
        Получение всего списка сущностей,
        списка по director_id,
        списка по genre_id
        """
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)

        if director_id:
            return movie_service.get_by_director_id(director_id)
        if genre_id:
            return movie_service.get_by_genre_id(genre_id)
        if year:
            return movie_service.get_by_year(year)

        all_movies = movie_service.get_all()
        return movie_schema.dump(all_movies), 200

    def post(self):
        """
        Создание новой записи
        """
        req_json = request.json
        movie_service.create(req_json)
        return 'Запись добавлена', 200


@movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    def get(self, movie_id: int):
        """
        Получение конкретной сущности по идентификатору
        """
        try:
            movie = movie_service.get_one(movie_id)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404

    def put(self, movie_id: int):
        """
        Полное обновление (всех полей) сущности по ID
        """
        req_json = request.json
        req_json['id'] = movie_id

        movie_service.update(req_json)

        return '', 200

    def delete(self, movie_id: int):
        """
        Удаление сущности по ID
        """
        return movie_service.delete(movie_id)
