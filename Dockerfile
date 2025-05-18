# Используем официальный Python-образ
FROM python:3.9-alpine3.16

# Устанавливаем необходимые пакеты
RUN apk add --no-cache \
    postgresql-dev \
    postgresql-libs \
    gcc \
    musl-dev \
    build-base \
    libffi-dev \
    openssl-dev
    
# Копируем файл зависимостей
COPY requirements.txt /temp/requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /temp/requirements.txt

# Копируем исходный код
COPY services /services

# Устанавливаем рабочую директорию
WORKDIR /services

# Открываем порт
EXPOSE 8000

# Создаем пользователя
RUN adduser --disabled-password services-user

# Переключаемся на пользователя
USER services-user