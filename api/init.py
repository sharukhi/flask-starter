# Imports variables from .env file

from dotenv import load_dotenv
import os



def init(): 
    load_dotenv()
    API_TOKEN = os.getenv('API_TOKEN')


