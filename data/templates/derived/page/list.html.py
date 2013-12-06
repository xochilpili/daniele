# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386337142.858907
_enable_loop = True
_template_filename = '/Users/xochilpili/Documents/Develop/python/pylons/DanieleChallenge/danielechallenge/templates/derived/page/list.html'
_template_uri = '/derived/page/list.html'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rows = context.get('rows', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n    <title>Daniele Challenge [Employees]</title>\n<style>\n#customers{\nfont-family:"Trebuchet MS", Arial, Helvetica, sans-serif;\nwidth:100%;\nborder-collapse:collapse;\n}\n#customers td, #customers th{\nfont-size:1em;\nborder:1px solid #98bf21;\npadding:3px 7px 2px 7px;\n}\n#customers th{\nfont-size:1.1em;\ntext-align:left;\npadding-top:5px;\npadding-bottom:4px;\nbackground-color:#A7C942;\ncolor:#ffffff;\n}\n#customers tr.alt td{\ncolor:#000000;\nbackground-color:#EAF2D3;\n}\n.menudes {\nposition: relative;\noverflow: hidden;\nwidth: 70%;\nmargin: 10px auto 10px;\nborder-radius: 8px;\nbackground: #025BA3;\ntext-align:center;\nfont-family: Tahoma, Geneva, sans-serif;\n}\n.menudes a {\ndisplay: inline-block;\nwidth: 15%; /* 100% dividido por el n\xfamero de elementos del men\xfa */\nbox-sizing: border-box;\npadding: 10px 5px;\ncolor: #fff;\ntext-decoration: none;\n}\n.marca {\nposition: absolute;\nbottom: 4px;\nleft: -12.5%; /* Al menos 1/2 del ancho de cada enlace */\nwidth: 12.5%; /* 1/2 del ancho de cada enlace */\nheight: 4px;\nbackground: #fff;\ntransition: 0.5s ease-in-out;\n}\n.menudes a:nth-child(1):hover ~ .marca {\nleft: 15.25%; /* 1/4 Ancho del enlace */\n}\n.menudes a:nth-child(2):hover ~ .marca {\nleft: 36.25%; /* 1/4 Ancho del enlace + 1 vez ancho enlace */\n}\n.menudes a:nth-child(3):hover ~ .marca {\nleft: 49.25%; /* 1/4 Ancho del enlace + 2 veces ancho enlace */\n}\n.menudes a:nth-child(4):hover ~ .marca {\nleft: 69.5%; /* 1/4 Ancho del enlace + 3 veces ancho enlace */\n}\n\n</style>\n</head>\n<body>\n<div class="menudes">\n<a href="/formtest/index">Inicio</a>\n<a href="/formtest/form">New Employee</a>\n<a href="/formtest/list">Employees</a>\n<a href="/formtest/contact">Contacto</a>\n<div class="marca"></div>\n</div>\n    <h1>List of Employees</h1>\n    \t<table id="customers">\n\t<tr>\n\t\t<th>Nombre</th>\n\t\t<th>Email</th>\n\t\t<th>Department</th>\n\t\t<th>DOF</th>\n\t\t<th>Salary</th>\n\t</tr>\n\t')
        # SOURCE LINE 86
        __M_writer(escape(rows))
        __M_writer(u'\n\t</table>\n\t<p>finish the list!</p>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


