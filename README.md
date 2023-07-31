# SKYMARKET
___
[![Python](https://img.shields.io/badge/python-3.9-orange)](https://www.python.org/downloads/release/python-394/)
[![Django](https://img.shields.io/badge/django-4.2.1-green)](https://docs.djangoproject.com/en/4.2/releases/4.0.1/)
[![Postgres](https://img.shields.io/badge/postgres-12.4-blue)](https://www.postgresql.org/docs/12/release-12-4.html)
[![Nginx](https://img.shields.io/badge/nginx-1.19-black)](https://www.postgresql.org/docs/12/release-12-4.html)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
___
#### Веб приложение для размещения объявлений о товарах
___
#### Для запуска проекта необходимо:
В качестве пакетного менеджера выбран pip.\
Запустить контейнеры из doker-compose файла для заппуска БД, frontend'а и nginx:
```shell
docker-compose -f infra/docker-compose.yaml up -d
```
Применить и сделать миграции:
```shell
python skymarket/manage.py makemigrations
python skymarket/manage.py migrate
```
Загрузка данные из фикстур в БД:
```shell
python skymarket/manage.py loadall
```
Запустить backend:
```shell
python skymarket/manage.py runserver
```
___
Доступ к frontend'у:
```
http://localhost:3000/
```
Доступ к backtend'у:
```
http://localhost:8000/
```
___
#### Swagger

Была выбрана библиотека [drf_spectacular](https://drf-spectacular.readthedocs.io/en/latest/readme.html#).
Доступ по следующим роутам:
```
/docs
/docs/schema
```

___
- [x] Функционал приложения реализован по документации указанной в `localhost:8000/api/redoc-tasks/`

