# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409099358.397031
_enable_loop = True
_template_filename = '/home/plablo/git/QuickCMS/quickcms/templates/derived/usuario/index.mako'
_template_uri = '/derived/usuario/index.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\nNombre de usuario: ')
        __M_writer(escape(c.usuario.username))
        __M_writer(u' </br>\nCorreo electr\xf3nico: ')
        __M_writer(escape(c.usuario.email))
        __M_writer(u' </br>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Informaci\xf3n del usuario:')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 2, "34": 3, "35": 3, "36": 4, "37": 4, "43": 2, "47": 2, "53": 47, "27": 0}, "uri": "/derived/usuario/index.mako", "filename": "/home/plablo/git/QuickCMS/quickcms/templates/derived/usuario/index.mako"}
__M_END_METADATA
"""
