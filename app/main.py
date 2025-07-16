from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/form_data", response_model=schemas.FormDataResponse)
def create_form(form: schemas.FormDataCreate, db: Session = Depends(get_db)):
    return crud.create_form_data(db=db, form_data=form)

@app.get("/form_data/{form_id}", response_model=schemas.FormDataResponse)
def get_form(form_id: int, db: Session = Depends(get_db)):
    form = crud.get_form_data_by_id(db, form_id)
    if not form:
        return {"detail": "Form not found"}
    return form