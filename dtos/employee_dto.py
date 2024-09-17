from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    emp_id: str
    name: str
    position: str
    salary: float


class EmployeePromote(BaseModel):
    new_position: str
    new_salary: float


class EmployeeDTO(BaseModel):
    emp_id: str
    name: str
    position: str
    salary: float

    class Config:
        orm_mode = True
        from_attributes = True
