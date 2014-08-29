# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409267020.25
_enable_loop = True
_template_filename = 'c:\\git\\QuickCMS\\quickcms\\templates/derived/contenidos/index.mako'
_template_uri = '/derived/contenidos/index.mako'
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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n')
        for item in c.contenidos:
            __M_writer(u'        <ul>\r\n            <li>T\xedtulo: ')
            __M_writer(escape(item.titulo))
            __M_writer(u'\r\n              <a href="')
            __M_writer(escape(h.url(controller ='contenido', action='crear_post',id=item.id)))
            __M_writer(u'">Editar</a>\r\n            </li>\r\n            <li>Usuario: ')
            __M_writer(escape(item.usuario.username))
            __M_writer(u' </li>\r\n            <li>Creado en: ')
            __M_writer(escape(item.creado))
            __M_writer(u' </li>\r\n            <li>Contenido: ')
            __M_writer(escape(item.texto))
            __M_writer(u' </li>\r\n        </ul>\r\n\r\n\r\n')
        __M_writer(u'\r\n<p><a href="')
        __M_writer(escape(h.url(controller ='usuarios', action='home')))
        __M_writer(u'">Home</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Contenidos:')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"65": 59, "34": 2, "35": 4, "36": 5, "37": 6, "38": 6, "39": 7, "40": 7, "41": 9, "42": 9, "43": 10, "44": 10, "45": 11, "46": 11, "47": 16, "48": 17, "49": 17, "59": 2, "55": 2, "27": 0}, "uri": "/derived/contenidos/index.mako", "filename": "c:\\git\\QuickCMS\\quickcms\\templates/derived/contenidos/index.mako"}
__M_END_METADATA
"""
