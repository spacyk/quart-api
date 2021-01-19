from os import environ


DB_HOST = environ.get('PGHOST', 'localhost')
DB_DATABASE = environ.get('PGDATABASE', 'quart_api')
DB_USER = environ.get('PGUSER', 'postgres')
DB_PASSWORD = environ.get('PGPASSWORD', '')
