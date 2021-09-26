from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#String de Conexión
SQLALCHEMY_DATABASE_URL = "postgresql://con_app_mensajeria:mensajeria@127.0.0.1/mensajeria"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()