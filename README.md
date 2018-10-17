1/ Clone the repository from this URL: https://github.com/immantra/Recipe_project
$ git clone https://github.com/immantra/Recipe_project

2/ Create and start a virtual environment

$ virtualenv env --no-site-packages 
$ source env/bin/activate

3/ create  a database (SQL) and modify the credentials (name-user-password-host-port) to access this database in the file  settings.py of the project in the section DATABASES

4/ Install the dependencies by running this command: (the dependencies are listed in this file)
$ pip install -r requirements.txt


5-Initialize your database: (xxxx is the number of the migration)
$ python manage.py makemigrations ingredients recipes
$ python manage.py sqlmigrate ingredients xxxx 
$ python manage.py sqlmigrate recipes xxxx 
 
$ python manage.py migrate

6- Create an admin account:
$ python ./manage.py createsuperuser

7- Run the development server to verify the application is working.
$ python ./manage.py runserver


===  If there is any problem, please contact me: iman.trabelssi@gmail.com ===
