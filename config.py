import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///volunteer_platform.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
