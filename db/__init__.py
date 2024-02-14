from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os


_mongodb_password = os.getenv('mongodb_password')
# connection_string = f'mongodb+srv://rrasmi070_portfolio:{_mongodb_password}@cluster0.i2ecse6.mongodb.net/?retryWrites=true&w=majority'
connection_string = 'mongodb://localhost:27017'
connection_client = MongoClient(connection_string)
