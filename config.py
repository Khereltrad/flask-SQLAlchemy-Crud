from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

user        = os.environ['MYSQL_USER']
password    = quote_plus(os.environ['MYSQL_PASSWORD'])
host        = os.environ['MYSQL_HOST']
port        = os.environ['MYSQL_PORT']
database    = os.environ['MYSQL_DATABASE']

DATABASE_CONECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'