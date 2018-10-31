deploy:
	docker-compose build
	docker-compose up -d
	docker-compose exec web python manage.py migrate

.PHONY: deploy
