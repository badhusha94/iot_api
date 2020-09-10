# iot_api

Required: python 3, mysql database, virtualenv (try to use virtual environment)
The Django, mysql, django rest framework packages will be installed from the requirements text file

Commands to run the project:

Open cmd from the folder where requirements_poc.txt is present
run cmd: pip install -r reuirements_poc.txt

Install MySQL database or change the Django Database connection settings to use your preferred database

Migrate Project:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

To Load fixtures:
python manage.py loaddata core/fixtures/sensorreading.json --app core.sensorreading

Sample GET url:

All data
http://127.0.0.1:8000/

Filter From and To dates
http://127.0.0.1:8000/?from=200915000000&to=200916235959

Filter To date
http://127.0.0.1:8000/?to=200911235959

Filter From date
http://127.0.0.1:8000/?from=200915000000
