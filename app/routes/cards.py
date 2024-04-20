from fastapi import APIRouter, Header
from fastapi import HTTPException, status, Depends

from jose import JWTError
from fastapi import Depends, HTTPException, status, Request
from app.utils.jwt_token import get_current_user
from app.utils.fake_database import cards
from app.routes.models import CardInfo

card = APIRouter()


@card.get("/card", tags=["Cards"],
          description="Требует Access Token в заголовке Authorization")
def get_info_card(authorization: str = Header(...), current_user: dict = Depends(get_current_user)) -> CardInfo:
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