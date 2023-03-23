FROM python:3.11-slim

# Instalar Pipenv
RUN pip3 install pipenv
RUN apt-get -y update; apt-get -y install curl 
# setear directorio de trabajo
ENV PROJECT_DIR /ofertas
WORKDIR $PROJECT_DIR

# Copy files to docker image
COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile
RUN pip install postgres

# Expose port for users microservice
EXPOSE 3003

CMD ["pipenv", "run", "python", "src/main.py"]
