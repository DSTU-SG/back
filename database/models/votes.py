from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass

class Votes(Base):
    __tablename__ = "votes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    header: Mapped[int] = mapped_column(String(100), nullable=False)
    text: Mapped[str] = mapped_column(String(400), nullable=False)
    consonants: Mapped[int] = mapped_column(nullable=False)
    dissenters: Mapped[int] = mapped_column(nullable=False)
    
class UserVotes(Base):
    __tablename__ = "user_votes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    vote_id: Mapped[int] = mapped_column(ForeignKey("votes.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False)
    vote: Mapped[bool] = mapped_column(Boolean())
    
