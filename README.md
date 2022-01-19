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
<img width="602" alt="Снимок экрана 2022-01-19 в 18 01 09" src="https://user-images.githubusercontent.com/82763714/150125706-e6a9df01-91cb-4fd7-9b47-bc1d90b22016.png">

### ToDo Tasks
<img width="588" alt="Снимок экрана 2022-01-19 в 18 01 39" src="https://user-images.githubusercontent.com/82763714/150125768-dc1225dd-2512-4134-801e-845ed8945453.png">
