# -*- coding: utf-8 -*-
import logging
import formencode
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from quickcms.lib.auth import ActionProtector
from repoze.what.predicates import is_user, has_permission, in_group
from quickcms.model.meta import Session
from quickcms.lib.base import BaseController, render
from quickcms.model.contenidos import Contenido, FormaNuevoContenido

log = logging.getLogger(__name__)

class ContenidoController(BaseController):

    @ActionProtector(has_permission('ver'))
    def index(self):
        """Regresa todos los contenidos"""

        c.contenidos = Session.query(Contenido).all()
        return render("/derived/contenidos/index.mako")

    def view(self,id):
        """Regresa la vista de un contenido"""

        c.contenido = Session.query(Contenido).get(id)
        return render("/derived/contenidos/view.mako")

    @ActionProtector(has_permission('edit'))
    def crear_post(self):
        """Regresa la forma para crear una nueva entrada en el blog"""

        return render("/derived/contenidos/nuevo.mako")

    @validate(schema=FormaNuevoContenido(), form='crear_post')
    @ActionProtector(has_permission('edit'))
    def guardar_contenido(self):
        """Guarda en la base de datos el post recibido por la forma"""

        contenido = Contenido()
        contenido.titulo = self.form_result["titulo"]
        contenido.texto = self.form_result["texto"]
        usuario = request.environ.get('repoze.who.identity')['user']
        contenido.usuario_id = usuario.id
        Session.add(contenido)
        Session.commit()
        return redirect(url(controller="contenido", action="view", id=contenido.id))
