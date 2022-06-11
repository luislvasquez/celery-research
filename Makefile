clean:
	docker-compose down -v

build:
	docker-compose build backend

up: build clean
	docker-compose up

run:
	docker-compose up