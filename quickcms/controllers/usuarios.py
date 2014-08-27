# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from quickcms.model.meta import Session
from quickcms.model.auth import AuthUser, FormaNuevoUsuario, AuthGroup
from quickcms.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UsuariosController(BaseController):
    def home(self):
        """ Redirige a index.mako"""
        if request.environ.get('repoze.who.identity') is not None:
            usuario = request.environ.get('repoze.who.identity')['user']
            grupos = usuario.auth_groups
            c.nombres_grupos = [g.name for g in grupos]

        return render("/index.mako")

    def index(self,id):
        # Return a rendered template
        #return render('/usuarios.mako')
        # or, return a string
        c.usuario = Session.query(Usuario).get(id)
        return render("/derived/usuario/index.mako")

    def crear(self):
        """Regresa la forma para crear un nuevo usuario"""
        return render("/derived/usuario/crear.mako")

    @validate(schema=FormaNuevoUsuario(), form='crear')
    def guardar_usuario(self):
        """Guarda el nuevo usuario en la base de datos"""
        usuario = AuthUser()
        usuario.username = self.form_result["username"]
        usuario.email = self.form_result["email"]
        usuario.password = self.form_result["password"]
        group = Session.query(AuthGroup).filter_by(name=u'usuarios').first()
        group.users.append(usuario)
        Session.add(usuario)
        Session.add(group)
        Session.commit()
        c.usuario = usuario
        session['flash'] = u"Se agregó el usuario."
        session.save()
        return render("/index.mako")
