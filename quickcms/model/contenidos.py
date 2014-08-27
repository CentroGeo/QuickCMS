# -*- coding: utf-8 -*-
import datetime
import formencode
from sqlalchemy import Column, Unicode, UnicodeText, Sequence, ForeignKey, TIMESTAMP
from sqlalchemy.types import Integer, Unicode, Text
from quickcms.model.meta import Base, Session

def now():
    return datetime.datetime.now()

class NombreUnico(formencode.validators.String):
    """Se encarga de validar que el titulo de la entrada sea unico"""

    def _to_python(self,value,state):
        nombre_valido = Session.query(Contenido).filter_by(titulo=value).first()
        if nombre_valido is not None:
            raise formencode.Invalid(
                "El título ya existe!!!",
                value,
                state
                )
        else:
            return value

class FormaNuevoContenido(formencode.Schema):
    """Se encarga de validar un nuevo contenido"""
    allow_extra_fields = True
    filter_extra_fields = True
    titulo = NombreUnico(not_empty=True)
    texto = formencode.validators.String(not_empty=True)


class Contenido(Base):
    """Representa una entrada en el blog."""

    __tablename__ = "contenidos"

    id = Column(Integer,Sequence('contenidos_seq_id'), primary_key=True)
    titulo = Column(Text, nullable = False)
    texto = Column(Text, nullable = False)
    creado = Column(TIMESTAMP(), default=now)
    editado = Column(TIMESTAMP(), default=None)
    usuario_id = Column(Integer, ForeignKey('auth_users.id'), nullable=False)
