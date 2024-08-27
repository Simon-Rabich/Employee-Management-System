from sqlalchemy import Column, String, Integer, Numeric, DateTime
from sqlalchemy.sql import func
from src.database.connection import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    emp_id = Column(String, index=True)
    name = Column(String, index=True)
    position = Column(String, index=True)
    salary = Column(Numeric)
    creation_time = Column(DateTime(timezone=True), server_default=func.now())
    last_update_time = Column(DateTime(timezone=True), onupdate=func.now())


my_dict = {'a': 1, 'b': 2, 'c': 3}
items_view = my_dict.items()