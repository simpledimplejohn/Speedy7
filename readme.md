# Django Forms
This app is a place to try out different ways of writing forms

## Creating forms with django


## Use this reposiotry
1. Clone the repository
2. add a .env file
    This will contain
    ```
    SECRET_KEY=
    API_KEY=
    LOG_LEVEL=debug
    ```
3. add a .gitignore file
4. run
    `python3 manage.py runserver 8000`

## Build this repository
1. create readme.md
2. create .gitignore
3. create .env
4. `django-admin startproject main_project .`
5. `python3 manage.py startapp sub_app`
6. add app to main_project/settings.py INSTALLED_APPS
7. add to main_project/urls.py 
8. Handle keys with decouple
    1. `pip install python-decouple`
    2. settings.py use config('name') to get the key from the .env file
        - remove any keys
9. Start Github
    1. `git init`
    2. make initial commit
    3. link to github.com
10. Finish app
    1. view.py
    2. urls.py
    3. index.html
    4. test and commit