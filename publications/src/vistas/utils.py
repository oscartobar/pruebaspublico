from datetime import datetime
import requests
import os

# Método para validar las fechas
def validateDates(planned_start_date, planned_end_date):
    # Verificar si la fecha de inicio es una fecha válida
    try:
        planned_start_date = datetime.strptime(planned_start_date, "%Y-%m-%d")
    except ValueError:
        return False

    # Verificar si la fecha de finalización es una fecha válida
    try:
        planned_end_date = datetime.strptime(planned_end_date, "%Y-%m-%d")
    except ValueError:
        return False

    # Verificar si la fecha de inicio es anterior a la fecha actual
    if planned_start_date < datetime.now():
        return False

    # Verificar si la fecha de fin es anterior a la fecha actual
    if planned_end_date < datetime.now():
        return False

    # Verificar si la fecha de finalización es anterior a la fecha de inicio
    if planned_end_date < planned_start_date:
        return False

    return True

# Validar token de usuario
def validateToken(self,request):
    token = str(request.headers.get('Authorization'))
    URL = "http://users:3000"
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(URL + "/users/me", headers=headers)
    if response.status_code >= 400:
        return 401
    return {
        'message': 'Token valido',
        "data": response.json()
    }, 200
