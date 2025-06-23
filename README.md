# 🛍️ Exchange Marketplace (Django)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-brightgreen.svg)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)](https://www.postgresql.org/)

**Exchange Marketplace** - это веб-платформа для обмена товарами между пользователями. Проект реализован на Django с использованием PostgreSQL в качестве базы данных.

## ✨ Основной функционал

### 🗂️ Объявления
- Просмотр списка всех активных объявлений
- Создание новых объявлений
- Удаление своих объявлений
- Фильтрация и поиск объявлений

### 🔄 Обмен товарами
- Создание предложений обмена
- Просмотр входящих предложений
- Принятие/отклонение предложений
- История совершенных обменов

### 👤 Пользователи
- Регистрация новых пользователей
- Аутентификация (логин/логаут)
- Личный кабинет
- Просмотр своих объявлений и предложений

## 🛠️ Технологический стек

- **Backend**: Django 5.2
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Аутентификация**: Django Auth
- **Деплой**: Docker (опционально)

## 🚀 Установка и запуск

### Предварительные требования
- Python 3.9+
- PostgreSQL 15+
- Virtualenv

### 1. Клонирование репозитория
```bash
git clone https://github.com/yourusername/exchange-marketplace.git
cd exchange-marketplace
