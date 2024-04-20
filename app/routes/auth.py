from typing import Optional
from fastapi import APIRouter
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import jwt, JWTError
from pydantic import BaseModel
from datetime import datetime, timedelta

from app.utils.check_password import verify_password
from app.utils.fake_database import fake_users_db
from config import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

import hashlib

auth = APIRouter()

o2auth_sheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

class AccessToken(BaseModel):
    access_token: str
    token_type: str

class UserCredentials(BaseModel):
    username: str
    password: str
    id: int

# Функция для создания JWT токена
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    # Токен как раз таки будет использоваться в т.ч. для идентификации пользователя
    to_encode = data.copy()
    if 'id' not in to_encode:
        raise ValueError("Отсутствует 'id' в данных для токена")
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@auth.post("/auth/login")
async def login(credentials: UserCredentials) -> AccessToken:
    # Здесь логика проверки учетных данных
    # Предположим, что у нас есть функция для проверки пароля
    # c хэшированным значением в базе данных
    user = fake_users_db.get(credentials.username)
    if not user or not verify_password(credentials.password, credentials.username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Создаем JWT токен, если учетные данные верны
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['username']}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}