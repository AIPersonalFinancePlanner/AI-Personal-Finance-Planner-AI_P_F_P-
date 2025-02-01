import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BANK_API_KEY = os.getenv('BANK_API_KEY')
    BANK_API_ENDPOINT = os.getenv('BANK_API_ENDPOINT', 'https://api.bank.example.com')
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')