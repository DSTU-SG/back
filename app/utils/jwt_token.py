from jose import jwt, JWTError
from typing import Optional
from datetime import datetime, timedelta

from config import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

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

def verify_token(token: str):
    try:
        # Декодирование токена
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Получение времени истечения токена
        exp = payload.get("exp")
        if not exp:
            return False, "Отсутствует время истечения токена."

        # Проверка времени истечения токена
        if datetime.now() >= datetime.fromtimestamp(exp):
            return False, "Время действия токена истекло."

        # Токен валиден
        return True, payload
    except JWTError as e:
        # Ошибка при декодировании токена
        return False, str(e)