DOCKER_COMPOSE=docker compose

build:
	$(DOCKER_COMPOSE) build

up: build
	$(DOCKER_COMPOSE) up

format:
	@echo Форматирование
	black .
	isort .

mypy:
	mypy --ignore-missing-imports lu_decomposition

install_req:
	python -m pip install --no-cache-dir -r dev-requirements.txt
