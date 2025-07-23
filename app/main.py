from fastapi import FastAPI, Depends
# from app.routers import user, food_log, exercise_log, suggestion
from app.core.config import settings
from app.core.database import SessionLocal
from sqlalchemy.orm import Session

# Importing routers
from app.routers import user

app = FastAPI(title="Health Tracker API")

app.include_router(user.router, prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/db_test")
def db_test(db: Session = Depends(get_db)):
    return {"status": "connected"}