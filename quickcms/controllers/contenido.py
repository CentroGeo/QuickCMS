# -*- coding: utf-8 -*-
import logging
import datetime
import formencode
from formencode import htmlfill
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from quickcms.lib.auth import ActionProtector
from repoze.what.predicates import is_user, has_permission, in_group
from quickcms.model.meta import Session
from quickcms.lib.base import BaseController, render
from quickcms.model.contenidos import Contenido, FormaNuevoContenido

log = logging.getLogger(__name__)

class FormencodeState(object):
    """
    Clase para pasar variables a los validadores en caso de ser necesario.
    """
    pass


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
    def crear_post(self,id=None):
        """Regresa la forma para crear una nueva entrada en el blog"""
        if id is not None:
            #estamos editando
            contenido = Session.query(Contenido).get(id)
            c.contenido = {'titulo':contenido.titulo,
                          'texto':contenido.texto,'id':contenido.id}
            return htmlfill.render(render("/derived/contenidos/nuevo.mako"),c.contenido)


        return render("/derived/contenidos/nuevo.mako")

#    @validate(schema=FormaNuevoContenido(), form='crear_post')
    @ActionProtector(has_permission('edit'))
    def guardar_contenido(self,id=None):
        """Guarda en la base de datos el post recibido por la forma"""

        if id is not None:
            contenido = Session.query(Contenido).get(id)
            titulo_original = contenido.titulo
            schema = FormaNuevoContenido() #contra que voy a validar
            ControllerState = FormencodeState() #el estado que le voy a pasar al validador
            if request.params['titulo']!=titulo_original:
                ControllerState.cambio = True #en este caso el validador debe checar que el nuevo nombre sea unico
            else:
                ControllerState.cambio = False

            try:
                form_result = schema.to_python(request.params,ControllerState)
            except formencode.validators.Invalid, error:
                c.contenido = {'titulo':request.params['titulo'],
                              'texto':request.params['texto']}
                return htmlfill.render(render("/derived/contenidos/nuevo.mako"),c.contenido,error)

            contenido.titulo = form_result['titulo']
            contenido.texto = form_result['texto']
            contenido.editado = datetime.datetime.now()
            Session.add(contenido)
            Session.commit()
            return redirect(url(controller="contenido", action="view", id=contenido.id))


        contenido = Contenido()
        contenido.titulo = self.form_result["titulo"]
        contenido.texto = self.form_result["texto"]
        usuario = request.environ.get('repoze.who.identity')['user']
        contenido.usuario_id = usuario.id
        Session.add(contenido)
        Session.commit()
        return redirect(url(controller="contenido", action="view", id=contenido.id))
