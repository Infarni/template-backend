FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml /app/
COPY poetry.lock /app/

RUN poetry install --without=dev,test

COPY . /app/

CMD ["sh", "scripts/start.sh"]
