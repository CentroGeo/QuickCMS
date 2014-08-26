# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409078203.233
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
        self = context.get('self', UNDEFINED)
        session = context.get('session', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\r\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\r\n<html>\r\n  <head>\r\n    <title>QuicCMS</title>\r\n')
        __M_writer(u'  </head>\r\n\r\n  <body>\r\n    <div class="content">\r\n      <h1 class="main">')
        __M_writer(escape(self.header()))
        __M_writer(u'</h1>\r\n')
        if session.has_key('flash'):
            __M_writer(u'    \t   <div id="flash"><p>')
            __M_writer(escape(session.get('flash')))
            __M_writer(u'</p></div>\r\n        ')

            del session['flash']
            session.save()
                    
            
            __M_writer(u'\r\n')
        __M_writer(u'      ')
        __M_writer(escape(next.body()))
        __M_writer(u'      <p class="footer">\r\n          QuickCMS\r\n      </p>\r\n    </div>\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 14, "37": 17, "38": 19, "39": 19, "40": 20, "46": 40, "16": 0, "24": 1, "25": 7, "26": 11, "27": 11, "28": 12, "29": 13, "30": 13, "31": 13}, "uri": "/base/base.mako", "filename": "C:\\Users\\alberto.porras\\Documents\\Git\\QuickCMS\\quickcms\\templates/base/base.mako"}
__M_END_METADATA
"""
