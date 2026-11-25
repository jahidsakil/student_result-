# ==========================================
# db.py  ->  Connection to the database
# ==========================================
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


SERVER_URL ="postgresql+psycopg2://sdgasdg_user:GIqIdyUNKhn2Cw5Y2LMPfABuVyIaLfdf@dpg-dc36koom7kps73dbq3mg-a.oregon-postgres.render.com/sdgasdg"



engine = create_engine(SERVER_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()



def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
