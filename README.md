# Курсовая работа №6
___
В качестве пакетного менеджера выбран `pip`
___
#### Для запуска проекта необходимо 
Запустить контейнеры из doker-compose файла для заппуска БД, frontend'а и nginx:
```shell
docker-compose -f ./infra/docker-compose.yaml up -d
```
Применить и сделать миграции:
```shell
./skymarket/manage.py makemigrations
./skymarket/manage.py migrate
```
Загрузка данные из фикстур в БД:
```shell
./skymarket/manage.py loadall
```
Запустить backend:
```shell
./skymarket/manage.py runserver
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
- [x] Работа выполнено согласно документации указанной в `localhost:8000/api/redoc-tasks/`
___
#### TODO LIST:
* tests
* CI/CD:
  * сделать Dockerfile для backend'a
  * переделать docker-compose
  * написать pipeline для GitHub Actions
* попробовать пересесть на poetry + pyenv
