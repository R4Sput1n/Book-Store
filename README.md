# Book-Store
## Main Features:
- Main Page listing all books in database
- Searching by `authors` and `book titles`.
- `Cart` feature
- `My account` page with books bought by user
- ability to download `pdfs` of bought books

## Installation:
Download and install [postgresql](https://www.postgresql.org/download/)

Create empty psql database [How to create empty database in postgresql](https://www.postgresql.org/docs/current/sql-createdatabase.html)

Install necessary packages via pip: `pip install -r requirements.txt`


## Configuration
Create `.env` file in your project's directory and inside put the following:
```text
SECRET_KEY = 'YOUR SECRET KEY'
DB_NAME = 'YOUR DB NAME'
DB_USER = 'YOUR DB USERNAME'
DB_PASSWORD = 'YOUR DB PASSWORD'
DB_HOST = '127.0.0.1'
DB_PORT = '5432'
```
You can easily generate secret key using  an online generator like [this one](https://djecrety.ir/)

### Migrations
Before adding anything to database make migrations first
Run command in terminal:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Fill the databse with dummy data
Run command in terminal
```bash
python manage.py loaddata dummy_data.json
```
### Create super user

Run command in terminal:
```bash
python manage.py createsuperuser
```

## Run
Execute: `python manage.py runserver`

Open up a browser and visit: http://127.0.0.1:8000/

### Adding more data
You can visit http://127.0.0.1:8000/admin, login as previously created superuser and there you can add more data
