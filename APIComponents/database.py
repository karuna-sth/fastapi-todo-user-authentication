from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base


SQL_ALCHEMY_DB = "sqlite:///./todos.db"


engine = create_engine(SQL_ALCHEMY_DB, connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
base = declarative_base()