# APLICACION DE USUARIOS

En esta carpeta se encuentra el codigo fuente, sus pruebas unitarias, y las colecciones de postman para el componete de usuarios.

Este proyecto hace uso de pipenv para gestión de dependencias y pytest para el framework de pruebas.

# Estructura de archivos
````
users
|____collection
| |____UsersApiLocal.postman_environment.json # Ambiente con variables de entorno para colección postman
| |____Users-API.postman_collection.json # Colección de postman únicamente para usuarios
|____pytest.ini # Configuración para pruebas unitarias con pytest
|____Dockerfile # Archivo dockerfile para configuración de compilación en docker
|____tests # Carpeta con archivos de pruebas
| |____conftest.py # Inicialización de fixture para uso en pruebas unitarias
| |______init__.py # Paquete de tests
| |____utils # Carpeta con pruebas clases de utilidad
| | |____test_utils.py # Clase con pruebas unitarias a clases de utilidad
| | |______init__.py
| |____model # Carpeta con pruebas clases de modelo
| | |____test_model.py # Clase con pruebas unitarias a clases de modelo
| | |______init__.py # Paquete pruebas de modelo
| |____view # Carpeta con pruebas clases de vistas
| | |____test_user_view.py # Clases con pruebas a clases de vista
| | |______init__.py # Paquete pruebas de vistas
|____README.md # Este archivo readme
|____Pipfile # Archivo de dependencias del microservicio
|____instance # Carpeta para base de datos local de pruebas unitarias
|____docker-compose.yml # Orquestador de microservicio de usuarios y base de datos
|____Pipfile.lock # Archivo lock de dependencias del microservicio
|____src # Carpeta de código fuente
| |______init__.py # Paquete de código fuente 
| |____utils # Carpeta de clases de utilidad
| | |______init__.py # Paquete de clases de utilidad
| | |____utils.py # Clase con utilidades para el microservicio
| |____model # Carpeta de clases de modelo
| | |____user_model.py # Modelo de entidad usuario
| | |______init__.py # Paquete de modelo
| |____view # Carpeta de clases de vistas
| | |______init__.py # Paquete de vistas
| | |____user_view.py # Vistas de la aplicación
| |____main.py # Configuración inicial y arranque de la aplicación
````
El archivo ci_pipeline.yml contiene el pipeline que ejecuta las pruebas.

## Como ejecutar localmente las pruebas

1. Install pipenv
2. Ejecutar pruebas
```
cd users
pipenv shell
pipenv install --dev
pipenv run pytest --cov=src -v -s --cov-fail-under=80
deactivate
```