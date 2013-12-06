# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386336191.183888
_enable_loop = True
_template_filename = '/Users/xochilpili/Documents/Develop/python/pylons/DanieleChallenge/danielechallenge/templates/derived/page/contact.html'
_template_uri = '/derived/page/contact.html'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<title>Daniele Challenge</title>\n<head>\n<style>\n.menudes {\nposition: relative;\noverflow: hidden;\nwidth: 70%;\nmargin: 10px auto 10px;\nborder-radius: 8px;\nbackground: #025BA3;\ntext-align:center;\nfont-family: Tahoma, Geneva, sans-serif;\n}\n.menudes a {\ndisplay: inline-block;\nwidth: 15%; /* 100% dividido por el n\xfamero de elementos del men\xfa */\nbox-sizing: border-box;\npadding: 10px 5px;\ncolor: #fff;\ntext-decoration: none;\n}\n.marca {\nposition: absolute;\nbottom: 4px;\nleft: -12.5%; /* Al menos 1/2 del ancho de cada enlace */\nwidth: 12.5%; /* 1/2 del ancho de cada enlace */\nheight: 4px;\nbackground: #fff;\ntransition: 0.5s ease-in-out;\n}\n.menudes a:nth-child(1):hover ~ .marca {\nleft: 15.25%; /* 1/4 Ancho del enlace */\n}\n.menudes a:nth-child(2):hover ~ .marca {\nleft: 36.25%; /* 1/4 Ancho del enlace + 1 vez ancho enlace */\n}\n.menudes a:nth-child(3):hover ~ .marca {\nleft: 49.25%; /* 1/4 Ancho del enlace + 2 veces ancho enlace */\n}\n.menudes a:nth-child(4):hover ~ .marca {\nleft: 69.5%; /* 1/4 Ancho del enlace + 3 veces ancho enlace */\n}\n\n</style>\t\n</head>\n<body>\n\t<div class="menudes">\n\t\t<a href="/formtest/index">Inicio</a>\n\t\t<a href="/formtest/form">New Employee</a>\n\t\t<a href="/formtest/list">Employees</a>\n\t\t<a href="/formtest/contact">Contacto</a>\n\t\t<div class="marca"></div>\n\t</div>\n\t<h1>Contact</h1>\n\t<p>Please contact us at: <span><small>xochilpili@gmail.com</small></span></p>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


