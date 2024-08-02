from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class EmployeeDTO(BaseModel):
    emp_id: str
    name: str
    position: str
    salary: float

    class Config:
        orm_mode = True
        from_attributes = True

