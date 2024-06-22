# Blog and Grog (Yatube)

## Описание

Веб-приложение для публикации постов с группами

## Запуск сервера для разработки

```sh
# !!! Linux: `python3` вместо `python` !!!

pip install -r requirements.txt # установка зависимостей

cd ./yatube/

python manage.py migrate # применение миграций БД

python manage.py createsuperuser # создание суперпользователя для администрирования

python manage.py runserver # запуск сервера на localhost:8000(по умолчанию)
```

## Автор

**Danil Tsarev**

*Почта для обратной связи* : DrSif@yandex.ru

**amozebus**

*Почта для обратной связи* : amozebus@gmail.com