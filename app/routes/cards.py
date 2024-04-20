from fastapi import APIRouter
from fastapi import HTTPException, status, Depends

from jose import JWTError
from fastapi import Depends, HTTPException, status, Request
from app.utils.jwt_token import decode_jwt_token
from app.utils.fake_database import cards
from app.routes.models import CardInfo

card = APIRouter()

async def get_current_user(request: Request):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
  
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise credentials_exception
    try:
        # Предполагается, что ваш токен начинается с 'Bearer '.
        token = auth_header.split(" ")[1]
        payload = decode_jwt_token(token)
        if payload is None:
            raise credentials_exception
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = {"user_id": user_id}
    except IndexError:
        raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    return token_data

@card.get("/card", tags=["Cards"],
          description="Требует Access Token в заголовке Authorization")
def get_info_card(current_user: dict = Depends(get_current_user)) -> CardInfo:
    user_id = current_user.get("user_id")
    if not user_id in cards.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found",
        )
    print(user_id)
    
    # Запросы к мнимой базе данных для получения информации по карте:
    data_card = cards.get(user_id)
    return data_card
    
    
    # Используйте user_id для получения информации о карте
    