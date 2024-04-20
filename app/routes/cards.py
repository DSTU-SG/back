from click import get_current_context
from fastapi import APIRouter
from fastapi import HTTPException, status, Depends

from app.routes.models import UserCredentials, AccessToken


card = APIRouter()


@card.get("/card")
def get_info_card(current_user: dict = Depends()):
    pass