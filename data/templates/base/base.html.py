# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386266502.119802
_enable_loop = True
_template_filename = u'/Users/xochilpili/Documents/Develop/python/pylons/DanieleChallenge/danielechallenge/templates/base/base.html'
_template_uri = u'/base/base.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<title>FormDemo</title>\n</head>\n<body>\n')
        # SOURCE LINE 6
        __M_writer(escape(next.body()))
        __M_writer(u'\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


