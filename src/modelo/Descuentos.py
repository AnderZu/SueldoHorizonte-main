import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Descuentos(Base):
    __tablename__ = 'descuentos'

    descuentos_faltas = Column(Integer)
    descuentos_tardanzas = Column(Integer)
    descuentos_total = Column(Integer)