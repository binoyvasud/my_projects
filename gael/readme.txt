
Modify the following in gael/settings.py 
DATABASES 
GAEL_PORT
GAEL_HOST
COUNT_MIN_LIMIT => For limiting the number of articles showing in a page
COUNT_MAX_LIMIT => Number of article showing in the what to read next section.

Run the following commands to make the database tables
python manage.py makemigrations  => this will create the files for the database tables 
python manage.py makemigrations article => this will create the files for the database tables 
python manage.py migrate => This will create the required tables in the selected database.
python manage.py createsuperuser => To create the super user.
python manage.py runserver = > To run the application
Then login to the admin panel using the username/password which you given while creating the super user.
Create the articles category, article and article images.
