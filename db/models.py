from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Text, TIMESTAMP, func, Index

Base = declarative_base()

class Post(Base):
    __tablename__ = "posts_clean"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    body = Column(Text)
    title_length = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    __table_args__ = (
        Index("idx_user_id", "user_id"),
    )