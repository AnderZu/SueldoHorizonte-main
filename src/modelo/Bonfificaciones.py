from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Bonifiaciones(Base):
    __tablename__ = 'bonifiaciones'

    pago_horas_extra = Column(Integer)
    movilidad = Column(Integer)
    bonificacion_suplementaria = Column(Integer)
    bonificacion_total = Column(Integer)
    remuneracion_computable = Column(Integer)