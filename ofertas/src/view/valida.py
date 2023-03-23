import requests
import os

class Validador():
   
    usuario = "User"
    
    def revisar(self,request):
        mitoken = str(request.headers.get('Authorization'))
        try:    
            URL = "http://users:3000"
            headers = {
            'Authorization': mitoken,
            'Content-Type': 'application/json'
            }
            data = {'app' : 'aaaaa'}
            resp = requests.get(URL + "/users/me", json=data, headers=headers)
            if resp.status_code >= 400:
                return 401
            
            return "",200
        except KeyError:
            print('Peticion invalida')

    
    
        return 200





