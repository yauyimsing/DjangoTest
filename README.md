# DjangoTest
Operation system: Linux
Language: Python
Database: MySQL

# Project step
1. enter the virtual environment
2. django-admin startproject DjangoProject
3. create MySQL database
	(mysql -uroot -p)(password:mysql)
	create database DjangoMySQL charset=utf8;
4. configurate setting.py with the database to be mysql
5. python manage.py startapp booktest
6. configurate setting.py with INSTALLED_APP adding app name
7. configurate booktest.models.py with add table class
8. python manage.py makemigrations
9. python manage.py migrate
