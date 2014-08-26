# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409075531.983
_enable_loop = True
_template_filename = 'C:\\Users\\alberto.porras\\Documents\\Git\\QuickCMS\\quickcms\\templates/derived/usuario/crear.mako'
_template_uri = '/derived/usuario/crear.mako'
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
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(escape(h.form_start(url(controller="usuarios",action="guardar_usuario"))))
        __M_writer(u'\n  Nombre de usuario:\n  ')
        __M_writer(escape(h.text(name='nombre_usuario')))
        __M_writer(u' <br />\n  Correo electr\xf3nico:\n  ')
        __M_writer(escape(h.text(name='email')))
        __M_writer(u' <br />\n  ')
        __M_writer(escape(h.submit(value='Guardar', name='commit')))
        __M_writer(u'\n')
        __M_writer(escape(h.form_end()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Nuevo usuario:')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 2, "35": 3, "36": 5, "37": 5, "38": 7, "39": 7, "40": 9, "41": 9, "42": 10, "43": 10, "44": 11, "45": 11, "51": 3, "55": 3, "27": 0, "61": 55}, "uri": "/derived/usuario/crear.mako", "filename": "C:\\Users\\alberto.porras\\Documents\\Git\\QuickCMS\\quickcms\\templates/derived/usuario/crear.mako"}
__M_END_METADATA
"""
