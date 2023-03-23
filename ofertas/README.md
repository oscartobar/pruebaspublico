# APLICACION DE OFERTAS

En esta carpeta se encuentra el codigo fuente, sus pruebas unitarias, y las colecciones de postman para el componete de ofertas. Las pruebas cubren el 82% del código.

Este proyecto hace uso de pipenv para gestión de dependencias y pytest para el framework de pruebas.

# Estructura
````
├── .github/workflows
|   └── ci_pipeline.yml # Configuración del pipeline
├── ofertas # Archivos de la aplicación de ofertas
|   ├── collections # Colecciones de postman
|   |    └── Ofertas.postman_collection.json # pruebas de postman en formato JSON
|   ├── instance # carpeta de base de datos local de pruebas
|   |    └── test.db # base de datos sqllite solo para pruebas
|   ├── src # código de la aplicación
|   |    └── modelos # base de datos sqllite solo para pruebas
|   |       └── __init__.py # clase constructora
|   |       └── modelos.py # clases de bases de datos
|   ├── utils # carpeta de utilitarios
|   |     └── clasebase.py # clase de pruebas
|   |     └── pruebas.py # funciones para iniciar la aplicacion
|   ├── view # carpeta con la logica 
|   |    └── valida.py # libreria de validaciones
|   |    └── vistas.py # libreria con la logica de la aplicacion
|   |    └── __init__.py # funciones de inicializacion
|   ├── tests # carpeta de base de datos local de pruebas
|   |    └── __init__.py # funciones de inicializacion
|   |    └── conftest.py # configuracion de las pruebas
|   |    └── test_main.py # pruebas de metodos transversales
|   |    └── test_vistas.py # pruebas de las vistas
|   ├── docker-compose.yml # configuracion de la aplicacion para funcionar junto al modulo de usuarios
|   ├── Dockerfile # configuracion del Docker con la aplicacion de ofertas
|   ├── Pipfile # Dependencias de la aplicación
|   ├── Pipfile.lock # Archivo lock de dependencias
|   ├── pytest.ini # Configuración de pruebas
└────── README.md # Estás aquí



````

En archivo ````ci_pipeline.yml```` contiene el pipeline que ejecuta las pruebas. Se recomienda revisar como está configurado y las notas en el.

## Como ejecutar localmente las pruebas

1. Install pipenv
2. Ejecutar pruebas
```
cd ofertas
pipenv shell
pipenv install --dev
pipenv run pytest --cov=src -v -s --cov-fail-under=80
deactivate
```