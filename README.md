1-Clone the repo

2-Create and start a a virtual environment
$ virtualenv env --no-site-packages
$ source env/bin/activate

3-Pip install requirements.txt
$ pip install -r requirements.txt

4-Enter your database settings in mysite/settings.py
5-Initialize your database.
$ python manage.py makemigrations ingredients recipes
$ python manage.py sqlmigrate ingredients xxxx 
$ python manage.py sqlmigrate recipes xxxx 
xxxx is the number of the migration
$ python manage.py migrate

6- create a new superuser for the admin.
$ python ./manage.py createsuperuser

7-Run the development server to verify everything is working.
$ python ./manage.py runserver








