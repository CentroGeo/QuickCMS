from sqlalchemy import *
from sqlalchemy.types import Integer, Unicode, Text
from sqlalchemy.orm import relation, backref, synonym
from sqlalchemy.orm.exc import NoResultFound
from quickcms.model.meta import Session
import formencode
from quickcms.model.meta import Base

import os
from hashlib import sha1
from datetime import datetime


class NombreUnico(formencode.validators.String):
    """Se encarga de validar que el nombre del usuario sea unico"""

    def _to_python(self,value,state):
        nombre_valido = Session.query(AuthUser).filter_by(username=value).first()
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
    username = NombreUnico(not_empty=True)
    email = formencode.validators.Email(not_empty=True)
    password = formencode.validators.String(not_empty=True)



group_permission_table = Table('auth_group_permissions', Base.metadata,
    Column('group_id', Integer,
            ForeignKey('auth_groups.id', onupdate='CASCADE',
            ondelete='CASCADE')),
    Column('permission_id', Integer,
            ForeignKey('auth_permissions.id',
            onupdate='CASCADE', ondelete='CASCADE'))
)
user_group_table = Table('auth_user_groups', Base.metadata,
    Column('user_id', Integer,
            ForeignKey('auth_users.id', onupdate='CASCADE', ondelete='CASCADE')),
    Column('group_id', Integer,
            ForeignKey('auth_groups.id', onupdate='CASCADE', ondelete='CASCADE'))
)

class AuthGroup(Base):
    __tablename__ = 'auth_groups'

    id = Column(Integer, primary_key=True,
                autoincrement=True)
    name = Column(Unicode(80), unique=True, nullable=False)
    #created = Column(mysql.DATE())

    users = relation('AuthUser', secondary=user_group_table, backref='auth_groups')

    def __repr__(self):
        return '<group: name=%s>' % self.name

    def __unicode__(self):
        return self.name

class AuthUser(Base):
    __tablename__ = 'auth_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Unicode(80), nullable=False)
    email = Column(Unicode(255), nullable = False)
    _password = Column('password', Unicode(80), nullable=False)
    posts = relation("Contenido",backref="usuario",cascade='all')

    @property
    def permissions(self):
        perms = set()
        for g in self.groups:
            perms = perms | set(g.permissions)
        return perms

    def _set_password(self, password):
        hashed_password = password

        if isinstance(password, unicode):
            password_8bit = password.encode('UTF-8')
        else:
            password_8bit = password

        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update(password_8bit + salt.hexdigest())
        hashed_password = salt.hexdigest() + hash.hexdigest()

        if not isinstance(hashed_password, unicode):
            hashed_password = hashed_password.decode('UTF-8')
        self._password = hashed_password

    def _get_password(self):
        return self._password

    password = synonym('_password', descriptor=property(_get_password,
                        _set_password))

    def validate_password(self, password):
        hashed_pass = sha1()
        hashed_pass.update(password + self.password[:40])
        return self.password[40:] == hashed_pass.hexdigest()

    def __repr__(self):
        return '<user: id="%s" username="%s" email="%s">' % (self.id,
                                                            self.username,
                                                            self.email)

    def __unicode__(self):
        return self.username

class AuthPermission(Base):
    __tablename__ = 'auth_permissions'

    id = Column(Integer, primary_key=True,
                autoincrement=True)
    name = Column(Unicode(80), unique=True, nullable=False)
    description = Column(Text)

    groups = relation(AuthGroup, secondary=group_permission_table,
                        backref='auth_permissions')

    def __unicode__(self):
        return self.permission_name
