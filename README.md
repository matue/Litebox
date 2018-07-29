## Необходимое ПО:

* [PostgreSQL 10](https://www.postgresql.org/download/windows/)
* [pgAdmin 4 v3.1](https://www.pgadmin.org/download/pgadmin-4-windows/)
* [python 3.6](https://www.python.org/downloads/release/python-360/)

## Шаги:
### Восстановление БД из дампа:

Для восстановления сперва нужно в pgAdmin создать роль входа "django/django" с ролью "postgres" а затем "пустую" БД PostgreSQL с именем "Litebox" и владельцем "django".

Восстановление происходит утилитой psql.
Пример:

```
psql.exe --host "localhost" --port "5432" -d Litebox -U django -f "D:\\Litebox.dumb"
```
В качестве владельца указан пользователь django.

### Установка дополнительных библиотек:

Следующие библиотеки должны присутствовать в PATH.
Если их нет то их нужно установить:

```
pip install django
pip install djangorestframework
pip install psycopg2
```
### Запуск сервера:

Запуск производится командой:

```
manage.py runserver
```

