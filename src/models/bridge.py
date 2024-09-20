from sqlalchemy import Column, String, DateTime
from src.database.connection import Base


class Bridge(Base):
    __tablename__ = "bridge"

    environment = Column(String, primary_key=True, nullable=False)
    version = Column(String)
    build_time = Column(DateTime, nullable=True)

