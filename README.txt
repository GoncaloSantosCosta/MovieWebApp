This is a group project as part of the Databases and Information Analysis course from the 
Masters in Biomedichal Engineering at the University of Coimbra. It marked our fist time 
using SQL, Django, HTML and CSS.

-The 'bd dados' file has the SQL code for 10 movies to be added in the PostGreSQL database

-Open 'settings.py' in the 'bdproject' folder, change the USERNAME and PASSWORD to match 
those of the pgadmin (postgres), and the NAME to the one from the database

-Open the terminal in the folder containing 'manage.py' and run the following commands to 
migrate the tables and start the Django web app server

python manage.py makemigrations brDbproject
python manage.py migrate
python manage.py runserver

-Connect to the app in the brower using:

localhost:8000/brDbproject