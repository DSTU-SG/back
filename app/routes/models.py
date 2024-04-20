from pydantic import BaseModel

class AccessToken(BaseModel):
    access_token: str
    token_type: str

class UserCredentials(BaseModel):
    username: str
    password: str

class CardInfo(BaseModel):
    number: str
    name: str
    date: str
    cvc: str
    
class Vote(BaseModel):
    text: str
