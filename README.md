# Awwards
# By Joan Nanjala.

Live site: View Site

# Description
This project allows users to post their projects for other users to rate according to design, usability, creativity and content.

# User Story
A user can view posted projects and their details.
A user can post a project to be rated/reviewed.
A user can rate/ review other users' projects.
Search for projects.
View projects overall score.
A user can view their profile page.
Setup and Installation
To get the project :

# Clone the repository:
* https://github.com/kangalah/Awwards
Install and activate Virtual
- python3 -m venv virtual - source virtual/bin/activate  
Navigate into the folder and install requirements with the command:
- pip install -r requirements.txt 

# Setup Database
SetUp your database User,Password, Host then make migrations:

- python manage.py makemigrations zawadi
Then Migrate:

-python manage.py migrate 

# Run the application
python manage.py runserver 

# Testing the application
* python manage.py test 
* Open the application on your browser 127.0.0.1:8000.

# Api Endpoints
* Profile api
* Posts api
* Technology used
* Python3.6
* Django 1.11.29
* Heroku

# Known Bugs
* When submitting a vote, the user has to click on post button twice or refresh the page for the change in average votes to be detected. I am working on still fixing this bug.
# Contact Information
* If you have any question or contributions, please email me at nyongesajoannanjala@gmail.com

# Copyright (c) 2019 Joan Nanjala.