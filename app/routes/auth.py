from fastapi import APIRouter
from fastapi import HTTPException, status, Depends

from datetime import timedelta

from app.utils.check_password import verify_password
from app.utils.fake_database import fake_users_db
from app.utils.jwt_token import create_access_token
from app.routes.models import UserCredentials, AccessToken

from config import ACCESS_TOKEN_EXPIRE_MINUTES

auth = APIRouter()


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
        data={"sub": user['id']}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}