FROM node:8.12-alpine as assets
COPY assets/package.json assets/yarn.lock /
RUN yarn
COPY assets /
CMD bash
RUN BUILD=1 /node_modules/.bin/webpack

FROM python:3.7-alpine3.8
RUN apk add --no-cache --update musl-dev gcc postgresql-dev linux-headers
COPY requirements.txt /src/
WORKDIR /src/
RUN pip install -r requirements.txt
COPY {{ cookiecutter.package_name }} /src/{{ cookiecutter.package_name }}
COPY manage.py /src/manage.py
COPY --from=assets /build/ /src/{{ cookiecutter.package_name }}/static/
CMD uwsgi --http :80 --wsgi-file /src/{{ cookiecutter.package_name }}/wsgi.py --processes 4
