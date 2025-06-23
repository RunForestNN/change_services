# 🛍️ Django Marketplace Exchange

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-brightgreen.svg)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://postgresql.org)
[![Celery](https://img.shields.io/badge/Celery-5.2-green.svg)](https://docs.celeryq.dev)
[![Redis](https://img.shields.io/badge/Redis-7.0-red.svg)](https://redis.io)

**Сервис обмена товарами** с возможностью публикации объявлений и управления предложениями обмена.

## ✨ Основной функционал

- **Объявления**
  - 📜 Просмотр списка всех объявлений
  - ➕ Добавление новых объявлений
  - ❌ Удаление своих объявлений

- **Обмен товарами**
  - 🔄 Создание предложений обмена
  - ✅ Принятие/отклонение предложений
  - ✉️ Уведомления о новых предложениях (Celery + Redis)

- **Аутентификация**
  - 👤 Регистрация новых пользователей
  - 🔐 Авторизация с сессиями
  - 🔄 Смена пароля

## 🛠 Технологический стек

| Компонент       | Технология       |
|----------------|------------------|
| Backend        | Django 5.2       |
| Database       | PostgreSQL       |
| Task Queue     | Celery + Redis   |
| Auth           | Django Sessions  |
| Email          | SMTP (Mail.ru)   |

## 🚀 Установка и запуск

### Предварительные требования
- Python 3.9+
- PostgreSQL 13+
- Redis 7.0+

### 1. Настройка окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
### 2.Установка зависимостей
```bash
pip install -r requirements.txt
```
### 3.Настройка базы данных
Создайте файл .env в корне проекта:
```bash
#Postgres
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

#Email
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=

#Redis
REDIS_URL=
```
### 4.Миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5.Запуск сервера
```bash
# Основной сервер
python manage.py runserver
```
### 6.Celery worker (в отдельном терминале)
```bash
celery -A testJob worker --pool=solo -l info
```
### 7.Redis (в отдельном терминале)
```bash
redis-server
```
### Docker-развертывание
```bash
docker-compose up --build
```
Система будет доступна на порту 8000.
