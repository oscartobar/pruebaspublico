# Proyecto Nube Grupo 9

En este proyecto se encuentran 4 microservicios construidos en Flask con bases de datos PostgreSQL, la compilación y despliegue de los artefactos se realiza via Docker, cada carpeta de los microservicios contiene un Dockerfile y en la raíz de proyecto se encuentra el archivo docker-compose.yml para el despliegue de todo el sistema en conjunto

# Estructura
````
|____collection-api.json # Colección de postman para probar microservicios
|____config.yaml # Archivo de configuración para evaluador
|____README.md # Archivo README con estructura y proceso de despliegue
|____.gitignore # Git Ignore
|____docker-compose.yml # Declaración de infraestructura de todos los microservicios
|____collection-api-env.postman_environment.json # Ambiente para colección de postman

ofertas
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

En archivo ````docker-compose.yml```` contiene la declaración de la infraestructura requerida para desplegar los microservicios y sus bases de datos incluyendo también redes y volúmenes de datos

## Como desplegar los microservicios

1. Ejecutar Docker Compose en la carpeta raíz con comando Build para compilar nuevos cambios si es necesario
2. Probar con colección de postman collection-api.json
```
docker-compose up --build
```