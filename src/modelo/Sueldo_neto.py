from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Sueldo_neto(Base)
    __tablename__ ='sueldo_neto'

    sueldo_neto = Column(Integer)
    bonificaciones = Column(Integer)
    descuentos = Column(Integer)
    id_trabajador = Column(Integer,ForeignKey('id.trabajador'),primary_key=True)
