FROM python:3.9.9
RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false
RUN mkdir /app
WORKDIR /app
ADD pyproject.toml poetry.lock /app/
RUN poetry install
ADD . /app