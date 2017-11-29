# Requirements
- Python (3.4, 3.5, 3.6)

# Installation
## No Docker
- Database
```sql
postgres=# CREATE USER ubuntu;
CREATE ROLE
postgres=# CREATE DATABASE cp OWNER ubuntu;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE cp to ubuntu;
GRANT
postgres=# \q
```
- Django project (Dev)
```bash
mv env_sample .env
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements/dev.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
