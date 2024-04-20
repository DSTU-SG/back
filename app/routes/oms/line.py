from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from pydantic import BaseModel

from app.utils.jwt_token import get_current_user


lines = APIRouter()

class OMSNumber(BaseModel):
    oms_number: str

fictive_services = {
    "1": "Больница",
    "2": "Больница для душевнобольных",
    "3": "Бэкендерная",
    "4": "ФРОНТ",
    "5": "Госуслуги",
    "6": "200"   
}

fictitious_people = {
    "1": "АБРАМОВИЧ",
    "2": "МАРК",
    "3": "УЛЬЯНОВ",
    "4": "КАЛИН"
}

@lines.get("/services", tags=["Services"])
def get_servives(authorization: str = Header(...),
                 current_user: dict = Depends(get_current_user)) -> JSONResponse:
    return JSONResponse(content=fictive_services)

@lines.get("/services/{service_id}", tags=["Services"])
def get_servives_by_id(service_id: str, authorization: str = Header(...),
                       current_user: dict = Depends(get_current_user)) -> JSONResponse:
    return JSONResponse(content=fictitious_people)

@lines.post("/services/{service_id}/{person_id}", tags=["Services"])
def send_OMS(service_id: str, person_id: str, oms_data = OMSNumber, authorization: str = Header(...),
             current_user: dict = Depends(get_current_user)) -> JSONResponse:
    pass
