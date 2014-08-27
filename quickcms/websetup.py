# -*- coding: utf-8 -*-
"""Setup the QuickCMS application"""
import logging

from quickcms.config.environment import load_environment
from quickcms.model.meta import Session, Base
from quickcms.model.contenidos import Contenido
from quickcms.model.auth import *

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup quickcms here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)

    # Drop and Create the tables if they don't already exist
    Base.metadata.drop_all(checkfirst=True, bind=Session.bind)
    Base.metadata.create_all(bind=Session.bind)

    #usuarios, etc por defecto
    u = AuthUser()
    u.username = u'test'
    u.password = u'test'
    u.email = u'test@example.com'
    Session.add(u)

    u2 = AuthUser()
    u2.username = u'chafita'
    u2.password = u'chafita'
    u2.email = u'chafita@example.com'
    Session.add(u2)

    g = AuthGroup()
    g.name = u'admin'
    g.users.append(u)
    Session.add(g)

    g_usuario=AuthGroup()
    g_usuario.name = u'usuarios'
    g_usuario.users.extend([u,u2])
    Session.add(g_usuario)

    p_ver = AuthPermission()
    p_ver.name = u'ver'
    p_ver.groups.append(g_usuario)
    Session.add(p_ver)

    p = AuthPermission()
    p.name = u'edit'
    p.groups.append(g)
    Session.add(p)
    Session.commit()

    post = Contenido()
    post.titulo = u"Post de inicio"
    post.texto = u"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    post.usuario_id = u.id

    Session.add(post)
    Session.commit()
