# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409163917.389
_enable_loop = True
_template_filename = u'C:\\Users\\alberto.porras\\Documents\\Git\\QuickCMS\\quickcms\\templates/base/base.mako'
_template_uri = u'/base/base.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        session = context.get('session', UNDEFINED)
        request = context.get('request', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\r\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\r\n<html>\r\n  <head>\r\n    <title>QuicCMS</title>\r\n')
        __M_writer(u'  </head>\r\n\r\n  <body>\r\n    <div class="content">\r\n        <div>\r\n')
        if request.environ.get('repoze.who.identity') is not None:
            __M_writer(u'                <p>Usuario: ')
            __M_writer(escape(request.environ.get('repoze.who.identity')['user'].username))
            __M_writer(u'</p>\r\n                <p><a href="')
            __M_writer(escape(h.url(controller ='login', action='logout_handler')))
            __M_writer(u'">Salir</a>\r\n                </p>\r\n')
        else:
            __M_writer(u'                <p><a href="')
            __M_writer(escape(h.url(controller ='login', action='login')))
            __M_writer(u'">Entrar</a>\r\n                <p><a href="')
            __M_writer(escape(h.url(controller ='usuarios', action='crear')))
            __M_writer(u'">Reg\xedstrate</a>\r\n')
        __M_writer(u'        </div>\r\n        <h1 class="main">')
        __M_writer(escape(self.header()))
        __M_writer(u'</h1>\r\n')
        if session.has_key('flash'):
            __M_writer(u'           <div id="flash"><p>')
            __M_writer(escape(session.get('flash')))
            __M_writer(u'</p></div>\r\n        ')

            del session['flash']
            session.save()
                    
            
            __M_writer(u'\r\n')
        __M_writer(u'        ')
        __M_writer(escape(next.body()))
        __M_writer(u'        <p class="footer">\r\n          QuickCMS\r\n        </p>\r\n    </div>\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "26": 1, "27": 7, "28": 12, "29": 13, "30": 13, "31": 13, "32": 14, "33": 14, "34": 16, "35": 17, "36": 17, "37": 17, "38": 18, "39": 18, "40": 20, "41": 21, "42": 21, "43": 22, "44": 23, "45": 23, "46": 23, "47": 24, "52": 27, "53": 29, "54": 29, "55": 30, "61": 55}, "uri": "/base/base.mako", "filename": "C:\\Users\\alberto.porras\\Documents\\Git\\QuickCMS\\quickcms\\templates/base/base.mako"}
__M_END_METADATA
"""
