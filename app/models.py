from sqlalchemy import Column, Integer, String
from .database import Base

class FormData(Base):
    __tablename__ = "form_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    address = Column(String)