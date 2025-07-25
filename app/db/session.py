from app.core.database import SessionLocal

# DB session 依賴注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()