from flask import request
from flask_restful import Resource
from utils.utils import validate_token
from utils.utils import InvalidAPIUsage
from model.route_model import Route, RouteSchema, db
from flask_jwt_extended import jwt_required
from datetime import timedelta
from datetime import datetime
import re

route_schema = RouteSchema()

class VistaPing(Resource):
    def get(self):
        return "pong"

class VistaRoutes(Resource):
    @validate_token()
    def post(self):
        try:
            sourceAirportCode = request.json["sourceAirportCode"]
            sourceCountry = request.json["sourceCountry"]
            destinyAirportCode = request.json["destinyAirportCode"]
            destinyCountry = request.json["destinyCountry"]
            bagCost = request.json["bagCost"]

            if not sourceAirportCode:
                raise InvalidAPIUsage("sourceAirportCode null", 400)
            if not sourceCountry:
                raise InvalidAPIUsage("sourceCountry null", 400)
            if not destinyAirportCode:
                raise InvalidAPIUsage("destinyAirportCode null", 400)
            if not destinyCountry:
                raise InvalidAPIUsage("destinyCountry null", 400)
            if bagCost <= 0:
                raise InvalidAPIUsage("bagCost null", 400)

        except Exception as ex:
            db.session.rollback()
            raise InvalidAPIUsage(format(ex), 400)

        route = Route.query.filter(Route.sourceAirportCode == sourceAirportCode, 
                                    Route.destinyAirportCode == destinyAirportCode
                                    ).first()
        if route is not None:
            expireAtRoute = route.createdAt + timedelta(days=30)
            if(expireAtRoute > datetime.now()):
                raise InvalidAPIUsage("Trayecto ya existe y esta activo", 412)

        new_route = Route(sourceAirportCode=sourceAirportCode,
                            sourceCountry=sourceCountry,
                            destinyAirportCode=destinyAirportCode, 
                            destinyCountry=destinyCountry,
                            bagCost=bagCost,
                            createdAt = datetime.now())
        
        db.session.add(new_route)
        db.session.commit()

        expireAt = new_route.createdAt + timedelta(days=30)
        result = {
            "id": new_route.id,
            "createdAt": new_route.createdAt.strftime('%Y-%m-%d %H:%M'),
            "expireAt": expireAt.strftime('%Y-%m-%d %H:%M'), 
        }

        return result , 201
       

    @validate_token()
    def get(self):
        try:
            resultado = Route.query.all()
            pfrom = request.args.get('from')
            if pfrom is not None:
                if not pfrom.isalpha():
                    raise Exception("Formato incorrecto") 
                resultado = filter(lambda route: route.sourceAirportCode == pfrom, resultado)
            pto = request.args.get('to')
            if pto is not None:
                if not pto.isalpha():
                    raise Exception("Formato incorrecto")
                resultado = filter(lambda route: route.destinyAirportCode == pto, resultado)
            when = request.args.get('when')
            if when is not None:
                 fecha = datetime.strptime(when, '%Y-%m-%d')
                 print(fecha)
                 resultado = filter(lambda route: route.createdAt <=  fecha, resultado)
 
            return [route_schema.dump(ca) for ca in resultado]

        except Exception as ex:
            db.session.rollback()
            raise InvalidAPIUsage(format(ex), 400)

class VistaRoute(Resource):
    @validate_token()
    def get(self, id_route):

        if id_route.isdigit() != True:
            raise InvalidAPIUsage("El id no es un número.", 400)

        route = Route.query.get(id_route)

        if route is None:
            raise InvalidAPIUsage("No existe el trayecto con ese identificador.", 404)
        
        return route_schema.dump(route)

       