# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409099576.286976
_enable_loop = True
_template_filename = '/home/plablo/git/QuickCMS/quickcms/templates/derived/contenidos/index.mako'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<ul>\n')
        for item in c.contenidos:
            __M_writer(u'        <ul>\n            <li>T\xedtulo: ')
            __M_writer(escape(item.titulo))
            __M_writer(u' </li>\n            <li>Usuario: ')
            __M_writer(escape(item.usuario.username))
            __M_writer(u' </li>\n            <li>Creado en: ')
            __M_writer(escape(item.creado))
            __M_writer(u' </li>\n            <li>Contenido: ')
            __M_writer(escape(item.texto))
            __M_writer(u' </li>\n        </ul>\n\n\n')
        __M_writer(u'\n</ul>\n')
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
{"source_encoding": "utf-8", "line_map": {"33": 2, "34": 4, "35": 5, "36": 6, "37": 6, "38": 7, "39": 7, "40": 8, "41": 8, "42": 9, "43": 9, "44": 14, "50": 2, "54": 2, "27": 0, "60": 54}, "uri": "/derived/contenidos/index.mako", "filename": "/home/plablo/git/QuickCMS/quickcms/templates/derived/contenidos/index.mako"}
__M_END_METADATA
"""
