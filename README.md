# deploying-django
Repo to accompany a 2 part series of blog posts about adding Postgres to your Django app and deploying to Heroku

## Related blog posts in [Agatha](https://medium.com/agatha-codes)
[Painless Postgres + Django](https://medium.com/@eleanorstrib/painless-postgresql-django-d4f03364989)

## Running the app
This app uses Django 1.11, Python 3.5, and PostgreSQL 9.6.

- Create and activate a virtual environment
- Run `pip install -r requirements.txt`
- Complete steps 1 & 2 in [this post](https://medium.com/@eleanorstrib/painless-postgresql-django-d4f03364989)
- Create environment variables for the database credentials and source them correctly in the settings.py file
- Migrate as shown in step 4 in [this post](https://medium.com/@eleanorstrib/painless-postgresql-django-d4f03364989)
