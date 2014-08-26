# -*- coding: utf-8 -*-
"""Setup the QuickCMS application"""
import logging

from quickcms.config.environment import load_environment
from quickcms.model.meta import Session, Base
from quickcms.model.usuario import Usuario
from quickcms.model.contenidos import Contenido

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup quickcms here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.create_all(bind=Session.bind)
    usuario = Usuario()
    usuario.nombre_usuario = u"admin"
    usuario.email = u"admin@quickCMS.org"
    Session.add(usuario)
    Session.commit()
    post = Contenido()
    post.titulo = u"Post de inicio"
    post.texto = u"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    post.usuario_id = usuario.id

    Session.add(post)
    Session.commit()
