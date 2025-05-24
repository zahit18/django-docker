# 🚀 Django Project with Docker & PostgreSQL

<img src="https://www.djangoproject.com/m/img/logos/django-logo-positive.png" alt="Django Logo" width="150" align="right">

A Django project template with Dockerized PostgreSQL and pgAdmin for database management.

## 🛠️ Setup Instructions

1. Clone Repository
2. Activate venv : `source .venv/Scripts/activate`
3. Run `docker-compose up`
4. Install requirements `pip install -r requirements.txt`
5. Create a super user `py manage.py createsuperuser`
6. Enter in `demo` directory
7. If you create Models run: `py manage.py makemigrations`
8. Run `py manage.py migrate`
9. Run `py manage.py runserver`


# Services
Django: http://localhost:8000
pgAdmin	http://localhost
Credentials into: docker-compose.yml

## Common Commands
Create new app: `python manage.py startapp app_name`