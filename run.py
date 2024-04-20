from app.routes.auth import *

from config import app

app.include_router(auth)