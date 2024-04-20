
from fastapi import HTTPException, status

from jose import jwt, JWTError
from typing import Optional
from datetime import datetime, timedelta, timezone

from config import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

# Функция для создания JWT токена
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    # Токен как раз таки будет использоваться в т.ч. для идентификации пользователя
    to_encode = data.copy()
    to_encode["sub"] = str(to_encode["sub"])
    if 'sub' not in to_encode:
        raise ValueError("Отсутствует 'id' в данных для токена")
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.now(timezone.utc) + timedelta(seconds=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Ручная проверка срока действия токена
        expire = payload.get("exp")
        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Expiration time (exp) claim is missing in the token.",
            )   
        expire_datetime = datetime.fromtimestamp(expire, tz=timezone.utc)
        if datetime.now(timezone.utc) > expire_datetime:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired"
            )
            
        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Could not validate credentials"
        ) from e