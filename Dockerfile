FROM python:3.9

RUN mkdir /app 
COPY app /app
COPY pyproject.toml /app

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# NB -w is the number of workers, it should be set to (2 c + 1) where c is the number of cores of the runing machine
ENTRYPOINT [ "gunicorn", "app.server:app","-w 3", "--bind 0.0.0.0:5000 ]
