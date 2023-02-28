from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Trabajador(Base):
    __tablename__ = 'trabajador'

    id_trabajador = Column(Integer, primary_key=True)
    nombre_trabajador = Column(String)
    dias_falta = Column(Integer)
    minutos_falta = Column(Integer)
    horas_extra = Column(Integer)

