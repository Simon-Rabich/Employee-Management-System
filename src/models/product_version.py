from sqlalchemy import Column, String, DateTime
from src.database.connection import Base


class ProductVersion(Base):
    __tablename__ = "product_version"

    environment = Column(String, primary_key=True, nullable=False)
    version = Column(String)
    build_time = Column(DateTime, nullable=True)

