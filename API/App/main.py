from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from database import SessionLocal , engine
import models


models.Base.metadata.create_all(bind = engine)
app = FastAPI()

#Dependency Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/hello')
def hello(db : Session = Depends(get_db)):
    return db.query(models.Employee).all()