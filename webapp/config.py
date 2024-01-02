import datetime
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.environ['API_KEY']
city=os.environ['CITY']
api_id=os.environ['API_ID_TELEGRAM']
api_hash=os.environ['API_HASH_TELEGRAM']
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),'..','webapp.db')
SECRET_KEY = "qwaszx1erdfcv2tyghbn3qaz4wsx5edc6"
REMEMBER_COOKIE_DURATION = datetime.timedelta(days=5)
