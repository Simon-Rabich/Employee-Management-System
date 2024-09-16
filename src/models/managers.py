from sqlalchemy import Column, String, Integer, Numeric, DateTime
from sqlalchemy.sql import func
from src.database.connection import Base


class Managers(Base):
    __tablename__ = "managers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    man_id = Column(String, index=True)
    name = Column(String, index=True)
    domain = Column(String, index=True)
    salary = Column(Numeric)
    creation_time = Column(DateTime(timezone=True), server_default=func.now())
    last_update_time = Column(DateTime(timezone=True), onupdate=func.now())