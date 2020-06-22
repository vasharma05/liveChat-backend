# Initial Setup
> Pull the code into your system
> Install python3 on your system

Run 
> pip install -r requirements.txt 

# Django setup
Shell or Terminal
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver

This will run the server at 127.0.0.1:8000 or localhost

* On the front page you will see an error page
* On /accounts/api/login This is the page where you request to check the login credentials
* On /accounts/api/signup This is the page where we send the details to signup a new user
* On /chatbot/api On GET Request, it sends a the chatbot details of the particular user.
* On /chatbot/api on POST Request, it creates or modifies the chatbot details of the user.
