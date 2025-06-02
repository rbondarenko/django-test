# django-test

- **Project**: test1
- **Application**: reimbursements

## To start

```shell
cd ~/projects
git clone git@github.com:rbondarenko/django-test.git
cd django-test
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install django==5.2.1
cd test1
python ./manage.py makemigration
python ./manage.py migrate
python ./manage.py createsuperuser
python ./manage.py runserver
```
- Go to http://localhost:8000/admin to add eligibility rules
- Go to http://localhost:8000/ to add submissions