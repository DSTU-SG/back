from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from app.routes.models import OMSNumber

from app.utils.jwt_token import get_current_user

import requests

lines = APIRouter()


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
def send_OMS(service_id: str, person_id: str, oms_data: OMSNumber, authorization: str = Header(...),
             current_user: dict = Depends(get_current_user)) -> JSONResponse:
    metadata_api = {
        "oms": oms_data.oms_number,        
        "user": current_user.get("user_id"),
        "service": service_id,
    }
    
    response = requests.post(
        "http://another-api.example.com/metadata_api",
        json=metadata_api,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Failed to send metadata: {response.text}"
        )
    
    return ({"200": "OK"})

