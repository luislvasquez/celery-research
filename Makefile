clean:
	docker-compose down -v

build:
	docker-compose build backend
	docker-compose build database	
	docker-compose build migration

up: build clean
	docker-compose up

run:
	docker-compose up