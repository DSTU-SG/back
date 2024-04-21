from fastapi import FastAPI


import platform
import secrets

app = FastAPI()

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class Config:
    DB_USER = "postgres"
    DB_PASS = "postgres"
    DB_NAME = "dgtu"
    DB_HOST = "localhost" 
    DB_PORT = "5432"