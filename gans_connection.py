
from dotenv import load_dotenv
import os

from sqlalchemy import create_engine

def get_database_connection():
    load_dotenv()
    mysql_pw = os.environ.get('MYSQL_PWS')

    user = 'root'
    pw = mysql_pw
    host = '127.0.0.1'
    port = '3306'
    db = 'gans'

    connection_str = f'mysql+pymysql://{user}:{pw}@{host}:{port}/{db}'
    engine = create_engine(connection_str)
    
    return engine