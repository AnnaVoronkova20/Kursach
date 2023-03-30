# Проектирование архитектуры приложения

# Реализация функциональной части

# Реализация серверной части

Реализованные endpoints:
- `/` - главная страница сайта
- `/docs` - документация к api методу
- `/schema` - получить схему api
- `/api/lu_decomposition` - выполнения LU-разложения матрицы

## Метод `/api/lu_decomposition` POST

Принимает в `body`:

- `matrix` - входящая матрица

```json
{
    "matrix": [
        [float, float, ...],
        [float, float, ...],
        [float, float, ...],
        ...
    ]
}
```

Возвращает:

- `L` - нижнетреугольная матрица с единичной диагональю
- `U` - верхнетреугольная матрица
- `input` - матрица, которую ввел пользователь

```json
{
    "L": [
        [float, float, ...],
        [float, float, ...],
        [float, float, ...],
        ...
    ],
    "U": [
        [float, float, ...],
        [float, float, ...],
        [float, float, ...],
        ...
    ],
    "input": [
        [float, float, ...],
        [float, float, ...],
        [float, float, ...],
        ...
    ]
}
```

В случае некорректной матрицы возвращается ответ с кодом `400`.

```json
{
    "msg": "bad matrix"
}
```

## Тест-кейсы



# Развертывание сервисной части

Был собран `Dockerfile`

```docker
FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . app
WORKDIR /app
RUN python ./manage.py migrate
EXPOSE 8000

ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

```

В данном файле был описан набор инструкций для сборки:
- `FROM python:3.9` - для установки базового образа собранного `python` версии `3.9`
- `COPY requirements.txt requirements.txt` - копирование зависимотей для работы программы
- `RUN pip install --no-cache-dir -r requirements.txt` - установка зависимостей без создания кэшурующей папки
- `COPY . app` - копирование кода программы в папку `app`
- `WORKDIR /app` - задание рабочей директории по пути `/app`
- `RUN python ./manage.py migrate` - запуск миграций
- `EXPOSE 8000` - открытие `8000` порта
- `ENTRYPOINT ["python", "./manage.py"]` - предоставляет команду с аргументами для вызова во время выполнения контейнера
- `CMD ["runserver", "0.0.0.0:8000"]` -  описывает команду с аргументами, которую нужно выполнить когда контейнер будет запущен

## Лог из консоли

![](./docs/running_docker_console.png)

## Запуск в docker-compose
![](./docs/running_docker_compose.png)

## Открытый сайт
![](./docs/running_docker_compose_site.png)

# Настройка оркестрации

Из-за того, что для реализации сервиса было необходимо сделать одностраничный сайт, было принято решение не использовать отдельный `frontend` сервер и выдавать статические файлы прямо с `backend` сервера.

```yaml
version: "3.8"

services:
  app:
    build: .
    container_name: django_app
    env_file:
      - .env
    restart: always
    ports:
      - "80:8000"

```

В файле `.env` передаются все необходимые переменные среды.

При возникновении ошибок контейнер будет перезапускаться.

Порты с контейнера прокидываются с локального `8000` порта на `80` порт.

Для удобства запуск приложения был создан `makefile`:
- `build` - сюорка образа
- `up` - запуск образа
- `format` - форматирование кода
- `mypy` - для проверки правильности оформления кода
- `install_req` - установка зависимотей для форматирования и проверки кода

Реализация:
```make
DOCKER_COMPOSE=docker-compose

build:
	$(DOCKER_COMPOSE) build

up: build
	$(DOCKER_COMPOSE) up

stop:
	docker-compose stop -t 0

format:
	@echo Форматирование
	black .
	isort .

mypy:
	mypy --ignore-missing-imports lu_decomposition

install_req:
	python -m pip install --no-cache-dir -r dev-requirements.txt
```
