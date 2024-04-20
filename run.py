from app.routes.auth import *
from app.routes.cards import *
from app.routes.votes import *

from database.db import engine
from database.models.votes import *

from config import app

app.include_router(auth)
app.include_router(card)
app.include_router(votes)

Base.metadata.create_all(engine)