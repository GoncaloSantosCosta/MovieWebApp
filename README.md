## Movie Web App

This was a group project developed as part of the Databases and Information Analysis course in the Master's in Biomedical Engineering at the University of Coimbra. It was our first experience using SQL, Django, HTML, and CSS.

### Setup instructions

- The `bd dados` file contains the SQL code needed to insert 10 movies into the PostgreSQL database.

- Open `settings.py` inside the `bdproject` folder and update the database configuration:
  - change `USERNAME` and `PASSWORD` to match your pgAdmin/PostgreSQL credentials;
  - change `NAME` to match the name of your database.

- Open a terminal in the folder containing `manage.py` and run the following commands to create the migrations, apply them, and start the Django development server:

```bash
python manage.py makemigrations brDbproject
python manage.py migrate
python manage.py runserver
