from pydantic import BaseModel, EmailStr
from typing import Optional

class FormDataCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None

class FormDataResponse(FormDataCreate):
    id: int

    class Config:
        orm_mode = True