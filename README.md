## Project

$This project is an API To Do List built from the Django framework + DRF

## Setup
      Look how easy it is to use:
      
          + Download the files from this repo
          + Change the directory to the folder where you downloaded files
          + For installing required packages, execute the following command in terminal:
          + create your .env environment variable and fill in the PostgreSQL database configuration
          
  ``` 
      $ git clone https://github.com/jennykucharski/django-todo-app.git
      $ cd ../path/to/the/file
      $ pip install -r requirements.txt
  ```

## Features

<ul>
<li><p>Register/p></li>
        http://localhost:port/api/dj-rest-auth/registration/
      
<li><p>Login</p></li>
        http://localhost:port/api/dj-rest-auth/login/
      
<li><p>Logout</p></li>
        http://localhost:port/api/dj-rest-auth/logout
      
<li><p>All TodoList </p></li>
        http://localhost:port/api/notes/
      
<li><p> ToDo Details </p></li>
       http://localhost:port/api/notes/<int:pk>/
</ul>

      After successful installation execute the following commands:

      ```
      $python manage.py migrate
      $python manage.py runserver
      ```



    
