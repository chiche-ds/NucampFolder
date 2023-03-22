from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

#connect to postgres database 

engine = create_engine('postgresql://postgress@localhost:5432/week3')
Session = sessionmaker(bind=engine)
base = declarative_base()