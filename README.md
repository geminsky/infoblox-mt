# infoblox-mt



This project is developed based on the assessment file shared via. mail by Infoblox

  - Postman is recommended for testing

You can also:
  - use browsable api
  - any other API interacting tool 

### Used Modules/Packages

* Django Rest Framework 
* django-filter
* Psycopg
* Django Rest Auth

### Installation

Install the dependencies

```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py user_data path/to/file.json
$ python manage.py runserver
```
*Note*: Change db settings in settings.py

### Request



| View | url |
| ------ | ------ |
| List View |api/all |
| Post view | api/new |

