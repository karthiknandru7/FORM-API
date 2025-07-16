from sqlalchemy.orm import Session
from . import models, schemas

def create_form_data(db: Session, form_data: schemas.FormDataCreate):
    db_form = models.FormData(**form_data.dict())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form
def get_form_data_by_id(db: Session, form_id: int):
    return db.query(models.FormData).filter(models.FormData.id == form_id).first()