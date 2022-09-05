# Дипломный проект "Сайт публикаций рецептов"
[![Django-app workflow](https://github.com/AlexNomak0607/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/AlexNomak0607/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

## Как запустить проект: 

 
Запустить:
```shell
docker-compose up -d
```

 

Применить миграции: 
```shell
docker-compose exec web python manage.py migrate 
```
 

Создать суперпользователя: 
```shell
docker-compose exec web python manage.py createsuperuser 
```
 

Cобрать статические файлы:
```shell
docker-compose exec web python collecstatic --no-input 
```

 

#### Основные доступные эндпоинты можно посмотреть по адресу http://localhost/redoc
#### Адрес проекта: http://84.252.143.219/
#### Admin: email youngbuck0607@mail.ru; password: 12345
