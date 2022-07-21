
from flask import request, json
from flask_restx import Resource, Namespace
from dao.model.director import DirectorModel, DirectorSchema
from container import director_service

director_schema = DirectorSchema(many=True)
director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):

    def get(self):
        """
        Получение всего списка сущностей,
        """
        all_directors = director_service.get_all()
        return director_schema.dump(all_directors), 200

    def post(self):
        """
         Создание новой записи
        """
        req_json = request.json
        director_service.create(req_json)
        return '', 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):

    def get(self, director_id: int):
        """
        Получение конкретной сущности по идентификатору
        """
        try:
            director = director_service.get_one(director_id)
            return director_schema.dump(director), 200
        except Exception as e:
            return "", 404

    def put(self, director_id: int):
        """
        Полное обновление (всех полей) сущности по ID
        """
        req_json = request.json
        req_json['id'] = director_id

        director_service.update(req_json)

        return '', 200

    def delete(self, director_id: int):
        """
        Удаление сущности по ID
        """
        return director_service.delete(director_id)