# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from quickcms.model.meta import Session
from quickcms.model.usuario import Usuario, FormaNuevoUsuario
from quickcms.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UsuariosController(BaseController):

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
        usuario = Usuario()
        usuario.nombre_usuario = self.form_result["nombre_usuario"]
        usuario.email = self.form_result["email"]
        Session.add(usuario)
        Session.commit()
        c.usuario = usuario
        session['flash'] = u"Se agregó el usuario."
        session.save()
        return render("/derived/usuario/index.mako")
