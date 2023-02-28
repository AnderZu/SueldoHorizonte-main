from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///aplicacion.sqlite')
##engine = create_engine('sqlite:///f:\\aplicacion.sqlite')
##engine = create_engine(r'sqlite:///f:\aplicacion.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
