# API KEY STEAM STORE(В разработке)

- API По продаже ключей STEAM, и регистрация/аутификачи и все с этим связаное реализованно через django-allauth и dj-rest-auth

## Функциональность

- Регистрация и аутентификация пользователей
- Подтверждение регистрации через электронную почту с отправкой ссылок
- Автоматическое удаление аккаунта через Celery, если пользователь не подтвердит почту в течение заданного времени


## Планы на будущее

- Интеграция Steam API для получения информации о играх
- Подключение платёжной системы для оплаты ключей
- Покрытие проекта юнит-тестами для повышения качества

# Стек технологий
- Django==4.2.19
- djangorestframework==3.14.0
- celery==5.2.7
- flower==2.0.1
- celery-singleton==0.3.1
- django-redis==5.2.0
- oauthlib==3.2.2
- django-allauth==65.2.0
- dj-rest-auth==7.0.0
- djangorestframework-jwt==1.11.0
- django-allauth[mfa]==65.2.0

## Установка и запуск (пример)

- docker compose run --rm wep-app sh -c "python manage.py migrate"

- docker compose run --rm wep-app sh -c "python manage.py test"

- docker compose up

