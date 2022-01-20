# p2-ToDo
   Here you can see code of the first assignment. Task was to build a ToDo application with authentication using Django Web Framework.
   
   Done by Shamshidin Sabina from SE-2008.

## Installation 
_Note: Before you work create a project folder and a venv folder, activate the corresponding environment_

**Django**
```
$ pip install django
```


## Usage

#### First, you need to create a ToDo database, which is populated when you use this commands:
```
$ python manage.py makemigrations home
$ python manage.py sqlmigrate home 0001
$ python manage.py migrate
```


#### Than, run the program 
```
$ python manage.py runserver
```

After running the program follow by this link: 
http://127.0.0.1:8000/login/

Next, you will see a login form, where you must enter the existing username and password in the database. Otherwise, it will not work.


## Examples 

### Login 

<img width="1496" alt="Снимок экрана 2022-01-20 в 20 50 00" src="https://user-images.githubusercontent.com/82763714/150361961-be57e56c-9d4b-4f96-b53c-78a4cf717dd2.png">


### ToDo Tasks!

[Uploading Снимок экрана 2022-01-20 в 20.50.54.png…]()
