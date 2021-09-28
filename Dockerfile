FROM python:3.9

RUN mkdir /app 
COPY . /app
COPY pyproject.toml /app

WORKDIR /app
RUN rm -r .venv 
RUN rm poetry.lock

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

#RUN apt-get install build-essential
RUN pip3 install poetry

#RUN poetry export -f requirements.txt --output requirements.txt

#RUN pip install -r requirements.txt 

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
EXPOSE 5000
# NB -w is the number of workers, it should be set to (2 c + 1) where c is the number of cores of the runing machine
ENTRYPOINT [ "gunicorn","-w 3", "-b", "0.0.0.0:5000",  "app.server:app" ]
