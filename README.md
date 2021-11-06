[![Python Version](https://img.shields.io/badge/python-3.8-hotpink.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0-hotpink.svg)](https://djangoproject.com)

This is a multiple user registration example in django that I created for ManezCo.

To run the project:
1. Clone the repository
```bash
git clone https://github.com/nusrat-borsha/Django-custom-registration.git
```
2. Install the requirements
```bash
pip install -r requirements.txt
```
3. Run migration
```bash
python manage.py migrate
```
4. Create super user
```bash
python manage.py createsuperuser
```
5. Run the server
```bash
python manage.py runserver
```

Book models and views are stored in the app called Book.
Accounts models and views are stored in the app called Accounts.

Media is stored in static/templates and it is hosted on an amazons3 bucket.

There are 3 types of users, Admin, Child and Adult. Admin does not have a register page and has to be made admin by a superuser in order to edit books. The admin can mark the books as Adult Content upon upload in order to restrict the books from the scope of a Child user.



