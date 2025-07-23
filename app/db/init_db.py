# db/init_db.py
from sqlalchemy import create_engine
from app.models.user import Base
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

# 建立所有定義的表格
Base.metadata.create_all(bind=engine)