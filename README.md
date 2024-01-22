
# Scripts

```bash
# Create super user
python manage.py createsuperuser

# Create migration for new Models
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Reset migrations
python manage.py showmigrations
python manage.py reset_migrations food 
python manage.py reset_migrations notes
python manage.py reset_migrations users
python manage.py showmigrations
python manage.py makemigrations food
python manage.py makemigrations notes
python manage.py makemigrations users
python manage.py migrate

```