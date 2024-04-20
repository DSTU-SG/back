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
    
    if 'Linux' in platform.system():
        DB_HOST = "host.docker.internal"
    else:
        DB_HOST = "localhost"    
        
    # DB_HOST = "host.docker.internal"
    # DB_HOST = "localhost"    
    DB_PORT = "5432"
