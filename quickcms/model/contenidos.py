import datetime
from sqlalchemy import Column, Unicode, UnicodeText, Sequence, ForeignKey, TIMESTAMP
from sqlalchemy.types import Integer, Unicode, Text
from quickcms.model.meta import Base

def now():
    return datetime.datetime.now()

class Contenido(Base):
    """Representa a un usuario en la base de datos."""

    __tablename__ = "contenidos"

    id = Column(Integer,Sequence('contenidos_seq_id'), primary_key=True)
    titulo = Column(Text, nullable = False)
    texto = Column(Text, nullable = False)
    creado = Column(TIMESTAMP(), default=now)
    editado = Column(TIMESTAMP(), default=None)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)