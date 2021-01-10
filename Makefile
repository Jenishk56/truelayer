start: build
	docker run --rm -v "$(shell pwd)":/app/ -p 5000:5000 --name pokemon-app pokemon-app python run.py

test: 
	docker run --rm -it -v "$(shell pwd):/app" --name pokemon-app-test pokemon-app python -m unittest

stop:
	docker stop backend-python-test && docker rm backend-python-test

build:
	docker build -t pokemon-app:latest .

rebuild: stop start
