
from flask import Flask, jsonify, request
from flask_restful import Resource
from .valida import Validador
from datetime import datetime
from modelos.modelos import db, OfertaSchema,Oferta

oferta_schema = OfertaSchema()

class VistaCreacion(Resource):

    def get(self):
        esvalido = Validador()
        if esvalido.revisar(request) == 401 :
            return "El token no es válido o está vencido.",401
        else:
            
            poffer = request.args.get('post')
            if poffer is None:
                return "Missing id offers",400
            
            if not poffer.isnumeric()  :
                return "Missing id offers",400
            
    
            publication = Oferta.query.filter_by(id=poffer)
            return [oferta_schema.dump(ca) for ca in publication]

                    
    def post(self):
        try:
            
            postId = request.json["postId"]
            description = request.json["description"]
            size=request.json["size"]
            fragile=request.json["fragile"]
            offer=request.json["offer"]
            
        
            esvalido = Validador()
            rta = esvalido.revisar(request)
            if rta == 401 :
                return "El token no es válido o está vencido.",401
            
            if offer < 0:
                return "Invalid Size",412
            
            if not size in("LARGE","MEDIUM","SMALL"):
                return "Invalid Size",412
            
            if offer is None or fragile is None or description is None or size is None:
                return "Empty Field", 412
            
            horaActual = datetime.today()
           
            fecha = datetime.now().isoformat
            miuswuario = "XXXXXX"
            new_offer = Oferta( 
                                postId=request.json["postId"], 
                                userId= miuswuario, 
                                description=request.json["description"], 
                                size=request.json["size"],
                                fragile=request.json["fragile"],
                                offer=request.json["offer"]
                                )
                            
            db.session.add(new_offer)
            db.session.commit()
            retorno = {"id":  new_offer.id , 
                        "userId": new_offer.userId , 
                        "createdAt": new_offer.createdAt.strftime('%Y-%m-%d %H:%M') }
             
            return retorno,201
        except KeyError:
            return "Los parametros no estan completos" ,400
            
  
    
class VistaConsulta(Resource):
   def get(self, offerid):
        try:
            esvalido = Validador()
            rta = esvalido.revisar(request)
            if offerid is None:
                return "El id no es un número.", 400
            
            try:
                if int(offerid) < 0: 
                    return "El id no es un número valido", 400
            except ValueError:
                    return "El id no es un número.", 400
                
            if rta == 401 :
                return "El token no es válido o está vencido.",401
            
            
                

            offeer = Oferta.query.get(offerid)

            if offeer is None:
                return "No existe" , 404
        except KeyError:  
            return "Los parametros no estan completos" ,400
        
        return oferta_schema.dump(offeer)

class VistaReset(Resource):
    def post(self):
        return "",200
  
    
  

class VistaPing(Resource):
    def get(self):
        return 'pong',200
    