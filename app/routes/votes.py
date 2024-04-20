from fastapi import APIRouter, Depends, Header, Request
from fastapi.responses import JSONResponse

import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import select

from database.db import engine
from database.models.votes import Votes, UserVotes

from app.utils.jwt_token import get_current_user
from app.routes.models import Vote

votes = APIRouter()

@votes.get("/votes", tags=["Votes"], description="Требует Access Token в заголовке Authorization")
def get_votes(authorization: str = Header(...), page: int = 1, count: int = 10, current_user: dict = Depends(get_current_user)):
    with Session(engine) as session:
        total_votes = session.query(Votes).all()
        
        votes = session.execute(
            select(Votes).offset((page - 1) * count).limit(count)
        ).scalars().all()
        
        return_votes = {}
        
        for vote in votes:
            user_vote = session.query(UserVotes).filter_by(vote_id=vote.id, user_id=current_user['user_id']).first()
            user_vote_status = None if not user_vote else user_vote.vote
            
            return_votes[vote.id] = {
                "id": vote.id,
                "text": vote.text,
                "consonants": vote.consonants,
                "dissenters": vote.dissenters,
                "user_vote": user_vote_status
            }
        
        return JSONResponse(content={"total": len(total_votes), "votes": return_votes})


@votes.post("/votes", tags=["Votes"])
def post_votes(request: Vote):
    text_data = request.text
    with Session(engine) as session:
        vote = Votes(text=text_data, consonants=0, dissenters=0)
        session.add(vote)
        session.commit()
    return {"200": "OK"}

@votes.post("/votes/consonants/{id_}", tags=["Votes"])
def send_vote_from_user(id_: int, authorization: str = Header(...), current_user: dict = Depends(get_current_user)):
    with Session(engine) as session:
        try:            
            user_vote = UserVotes(vote_id=id_, user_id=int(current_user["user_id"]), vote=True)
            session.add(user_vote)
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            session.rollback()    
    return {"200": "OK"}
    
@votes.post("/votes/dissenters/{id_}", tags=["Votes"])
def send_vote_from_user(id_: int, authorization: str = Header(...), current_user: dict = Depends(get_current_user)):
    with Session(engine) as session:
        try:
            user_vote = UserVotes(vote_id=id_, user_id=int(current_user["user_id"]), vote=False)
            session.add(user_vote)
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
    return {"200": "OK"}