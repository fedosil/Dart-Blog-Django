# Dart Blog

The project for study Django.

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python -m venv venv
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   python manage.py migrate
   python manage.py loaddata blog/fixtures/category.json
   python manage.py loaddata blog/fixtures/tag.json
   python manage.py loaddata blog/fixtures/post.json
   python manage.py collectstatic
   python manage.py runserver 
   ```

4. To work with the admin panel, you must create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
