# ==========================================
# db.py  ->  Connection to the database
# ==========================================
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


SERVER_URL = "postgresql+psycopg2://training_r6gf_user:RXPh6cQ5BTM3Z039FwYNVWMxi6Wy8ZQp@dpg-dc36b5om7kps73daqjm0-a.oregon-postgres.render.com/training_r6gf"



engine = create_engine(SERVER_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()



def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
