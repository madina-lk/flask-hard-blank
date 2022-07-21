
from flask import request
from flask_restx import Resource, Namespace
from dao.model.genre import GenreModel, GenreSchema
from container import genre_service

genre_schema = GenreSchema(many=True)           # создание экземпляра схемы

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        """
        Получение всего списка сущностей,
        """
        all_genre = genre_service.get_all()
        return genre_schema.dump(all_genre), 200

    def post(self):
        """
         Создание новой записи
        """
        req_json = request.json
        genre_service.create(req_json)
        return '', 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        try:
            genre = genre_service.get_one(genre_id)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return "", 404

    def put(self, genre_id: int):
        """
        Полное обновление (всех полей) сущности по ID
        """
        req_json = request.json
        req_json['id'] = genre_id

        genre_service.update(req_json)

        return '', 200


    def delete(self, genre_id: int):
        """
        Удаление сущности по ID
        """
        return genre_service.delete(genre_id)

