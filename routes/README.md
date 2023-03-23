# APLICACION DE TRAYECTOS

En esta carpeta se encuentra el codigo fuente, sus pruebas unitarias, y las colecciones de postman para el componete de trayectos.

Este proyecto hace uso de pipenv para gestión de dependencias y pytest para el framework de pruebas.

# Estructura de archivos
````
routes
|____pytest.ini # Configuración para pruebas unitarias con pytest
|____Dockerfile # Archivo dockerfile para configuración de compilación en docker
|____tests # Carpeta con archivos de pruebas
| |____conftest.py # Inicialización de fixture para uso en pruebas unitarias
| |____test_routes.py # Pruebas unitarias 
| |______init__.py # Paquete de tests
|____README.md # Este archivo readme
|____Pipfile # Archivo de dependencias del microservicio
|____docker-compose.yml # Orquestador de microservicio de trayectos y base de datos
|____Pipfile.lock # Archivo lock de dependencias del microservicio
|____src # Carpeta de código fuente
| |______init__.py # Paquete de código fuente 
| |____utils # Carpeta de clases de utilidad
| | |______init__.py # Paquete de clases de utilidad
| | |____utils.py # Clase con utilidades para el microservicio
| |____model # Carpeta de clases de modelo
| | |____route_model.py # Modelo de entidad route
| | |______init__.py # Paquete de modelo
| |____view # Carpeta de clases de vistas
| | |______init__.py # Paquete de vistas
| | |____route_view.py # Vistas de la aplicación
| |____main.py # Configuración inicial y arranque de la aplicación
````
El archivo ci_pipeline.yml contiene el pipeline que ejecuta las pruebas.

## Como ejecutar localmente las pruebas

1. Install pipenv
2. Ejecutar pruebas
```
cd routes
pipenv shell
pipenv install --dev
pipenv run pytest --cov=src -v -s --cov-fail-under=80
deactivate
```