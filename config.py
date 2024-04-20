from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import platform
import secrets

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class Config:
    DB_USER = "postgres"
    DB_PASS = "postgres"
    DB_NAME = "dgtu"
    DB_HOST = "db"  # Используйте имя сервиса Docker в качестве хоста
    DB_PORT = "5432"