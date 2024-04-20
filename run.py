from app.routes.auth import *
from app.routes.cards import *

from config import app

app.include_router(auth)
app.include_router(card)