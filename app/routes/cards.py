from fastapi import APIRouter
from fastapi import HTTPException, status, Depends

from app.routes.models import UserCredentials, AccessToken


cards = APIRouter()

