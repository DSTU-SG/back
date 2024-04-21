from app.routes.auth import *
from app.routes.cards import *
from app.routes.votes import *
from app.routes.oms.line import lines

from database.db import engine
from database.models.votes import *

from fastapi.middleware.cors import CORSMiddleware

from config import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
app.include_router(card)
app.include_router(votes)
app.include_router(lines)

Base.metadata.create_all(engine)