import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from quickcms.model.meta import Session
from quickcms.lib.base import BaseController, render
from quickcms.model.contenidos import Contenido

log = logging.getLogger(__name__)

class ContenidoController(BaseController):

    def index(self):
        """Regresa todos los contenidos"""
        c.contenidos = Session.query(Contenido).all()
        return render("/derived/contenidos/index.mako")
