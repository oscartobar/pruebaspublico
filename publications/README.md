# APLICACION DE PUBLICACIONES

En esta carpeta se encuentra el codigo fuente, sus pruebas unitarias, y las colecciones de postman para el componente de publicaciones.

Este proyecto hace uso de pipenv para gestión de dependencias y pytest para el framework de pruebas.

# Estructura de archivos
````
publications
|____pytest.ini # Configuración para pruebas unitarias con pytest
|____Dockerfile # Archivo dockerfile para configuración de compilación en docker
|____test # Carpeta con archivos de pruebas
| |____conftest.py # Inicialización de fixture para uso en pruebas unitarias
| |____init__.py # Paquete de tests
| | |__test_create_publication.py # Clase con pruebas unitarias a crear una publicion
| | |__test_publication_detail.py # Clase con pruebas unitarias a detalle de una publicacion 
| | |__test_publication_list.py # Clase con pruebas unitarias a lista de publicaciones
|____README.md # Este archivo readme
|____Pipfile # Archivo de dependencias del microservicio
|____docker-compose.yml # Orquestador de microservicio de publicaciones y base de datos
|____Pipfile.lock # Archivo lock de dependencias del microservicio
|____src # Carpeta de código fuente
| |______init__.py # Paquete de código fuente 
| |____modelos # Carpeta de clases de modelo
| | |____modelos.py # Modelo de entidad publicacion
| | |______init__.py # Paquete de publicacion
| |____vistas # Carpeta de clases de vistas
| | |______init__.py # Paquete de vistas
| | |____vistas.py # Vistas de la aplicación
| | |____utils.py # Clase con utilidades para el microservicio
| |____app.py # Configuración inicial y arranque de la aplicación
````

## Como ejecutar localmente las pruebas

1. Install pipenv
2. Ejecutar pruebas
```
cd publications
pipenv shell
pipenv install --dev
pipenv run pytest --cov=src -v -s --cov-fail-under=80
deactivate
```
