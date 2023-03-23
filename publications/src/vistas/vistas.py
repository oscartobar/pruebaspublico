from datetime import datetime
from modelos.modelos import db, Publication
from flask import request
from flask_restful import Resource
from . import utils
import logging

logging.basicConfig(level=logging.DEBUG)

publications_schema = Publication()

class CreatePublication(Resource):
    def post(self):

        try:
            user = utils.validateToken(self, request)
            if (user == 401) :
                return {'message': 'Token invalid'}, 401
            userId = user[0]['data']['id']
        except ValueError:
            return {'message': 'Token invalid'}, 401

        try:
            # Obtiene los datos de la publicacion a partir del cuerpo de la petición
            routeId = request.json['routeId']
            plannedStartDate = None
            if request.json['plannedStartDate']:
                plannedStartDate = datetime.strptime(request.json['plannedStartDate'], '%Y-%m-%d')
            plannedEndDate = None
            if request.json['plannedEndDate']:
                plannedEndDate = datetime.strptime(request.json['plannedEndDate'], '%Y-%m-%d')
            if plannedStartDate is None or plannedEndDate is None or routeId is "":
                return {'message': 'Mandatory data is missing'}, 400
            if utils.validateDates(request.json['plannedStartDate'], request.json['plannedEndDate']) is False:
                return {'message': 'Incorrect dates'}, 412
        except KeyError:
            return {'message': 'Mandatory data is missing'}, 400





        # Crea una nueva publicacion
        pub = Publication(routeId=routeId, userId=userId, plannedStartDate=plannedStartDate, plannedEndDate=plannedEndDate)

        # Guarda la publicacion en la base de datos
        db.session.add(pub)
        db.session.commit()

        return {
            'message': 'Post created successfully',
            "data": {
                "id": pub.id,
                "userId": pub.userId,
                "createdAt": pub.createdAt.isoformat()
            }
        }, 201

class PublicationsList(Resource):
    def get(self):
        try:
            user = utils.validateToken(self, request)
            if (user == 401) :
                return {'message': 'Token invalid'}, 401
            userId = user[0]['data']['id']
        except ValueError:
            return {'message': 'Token invalid'}, 401

        # Obtener los parámetros del servicio POST
        when = request.args.get('when')
        route = request.args.get('route')
        filterme = request.args.get('filter')

        # Realizar una consulta a la base de datos basada en los parámetros
        if filterme and filterme == 'me':
            # Si el filtro es "me", retornar solo las publicaciones del usuario actual
            publications = Publication.query.filter(Publication.userId == userId)
        else:
            # Si no hay filtro o el filtro es diferente de "me", retornar todas las publicaciones
            publications = Publication.query.all()

        # Filtrar las publicaciones por fecha y ruta, si se especificaron
        if when:
            try:
                when = datetime.strptime(when + "T00:00:00", "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                return {'message': 'Value of when is not date'}, 400
            publications = [publication for publication in publications if publication.plannedStartDate == when]

        if route:
            try:
                route = int(route)
            except ValueError:
                return {'message': 'Route is not integer'}, 400
            publications = [publication for publication in publications if publication.routeId == route]

        # Serializar las publicaciones y retornarlas en formato JSON
        publication_list = []
        for publication in publications:
            publication_list.append({
                'id': publication.id,
                'routeId': publication.routeId,
                'userId': publication.userId,
                'plannedStartDate': publication.plannedStartDate.isoformat(),
                'plannedEndDate': publication.plannedEndDate.isoformat(),
                'createdAt': publication.createdAt.isoformat()
            })

        return publication_list, 200

class PublicationDetail(Resource):
    def get(self, id_post):

        if (utils.validateToken(self, request) == 401) :
            return {'message': 'Token invalid'}, 401

        try:
            id_post = int(id_post)
        except ValueError:
            return {'message': 'Post id is not integer'}, 400

        publication = Publication.query.filter_by(id=id_post).first()
        if publication:
            return {
                'message': 'Successfully',
                'data': {
                        'id': publication.id,
                        'routeId': publication.routeId,
                        'userId': publication.userId,
                        'plannedStartDate': publication.plannedStartDate.strftime("%Y-%m-%d %H:%M:%S"),
                        'plannedEndDate': publication.plannedEndDate.strftime("%Y-%m-%d %H:%M:%S"),
                        'createdAt': publication.createdAt.strftime("%Y-%m-%d %H:%M:%S")
                    }
            }, 200
        else:
            return {'message': 'Post id not exist'}, 404

class Ping(Resource):
    def get(self):
        return "Pong"


