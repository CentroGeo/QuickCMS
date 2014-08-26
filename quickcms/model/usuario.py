from sqlalchemy import Column, Unicode, UnicodeText, Sequence
from sqlalchemy.orm import relation
from sqlalchemy.types import Integer, Unicode
from quickcms.model.meta import Base, Session
import formencode

class NombreUnico(formencode.validators.String):
    """Se encarga de validar que el nombre del usuario sea unico"""

    def _to_python(self,value,state):
        nombre_valido = Session.query(Usuario).filter_by(nombre_usuario=value).first()
        if nombre_valido is not None:
            raise formencode.Invalid(
                "El nombre de usuario ya existe!!!",
                value,
                state
                )
        else:
            return value

class FormaNuevoUsuario(formencode.Schema):
    """Se encarga de validar la forma de nuevo usuario"""
    allow_extra_fields = True
    filter_extra_fields = True
    nombre_usuario = NombreUnico(not_empty=True)
    email = formencode.validators.Email(not_empty=True)


class Usuario(Base):
    """Representa a un usuario en la base de datos."""

    __tablename__ = "usuarios"

    id = Column(Integer,Sequence('usuarios_seq_id'), primary_key=True)
    nombre_usuario = Column(Unicode(255), nullable = False)
    email = Column(Unicode(255), nullable = False)
    posts = relation("Contenido",backref="usuario",cascade='all')
