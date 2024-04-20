from pydantic import BaseModel

class AccessToken(BaseModel):
    access_token: str
    token_type: str

class UserCredentials(BaseModel):
    username: str
    password: str
    id: int