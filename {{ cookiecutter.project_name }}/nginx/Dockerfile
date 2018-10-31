FROM {{ cookiecutter.project_name }}_web as web
RUN python manage.py collectstatic --noinput

FROM nginx:alpine
COPY etc /etc
COPY --from=web /var/www /var/www
