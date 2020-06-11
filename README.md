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
* On /accounts/api/users You will see a list of all the users
* On /accounts/api/company You will see a list of all the company details along with the user details
* On /accounts/login This is the page where you request to check the login credentials
* On /accounts/signup This is the page where we send the details to signup a new user
