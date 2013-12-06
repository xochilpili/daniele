# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386336548.721506
_enable_loop = True
_template_filename = '/Users/xochilpili/Documents/Develop/python/pylons/DanieleChallenge/danielechallenge/templates/derived/page/simpleform.html'
_template_uri = '/derived/page/simpleform.html'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<title>Daniele Challenge [AddEm]</title>\n<head>\n<style>\n\nform    {\nbackground: -webkit-gradient(linear, bottom, left 175px, from(#CCCCCC), to(#EEEEEE));\nbackground: -moz-linear-gradient(bottom, #CCCCCC, #EEEEEE 175px);\nmargin:auto;\nposition:relative;\nwidth:550px;\nheight:450px;\nfont-family: Tahoma, Geneva, sans-serif;\nfont-size: 14px;\nfont-style: italic;\nline-height: 24px;\nfont-weight: bold;\ncolor: #09C;\ntext-decoration: none;\n-webkit-border-radius: 10px;\n-moz-border-radius: 10px;\nborder-radius: 10px;\npadding:10px;\nborder: 1px solid #999;\nborder: inset 1px solid #333;\n-webkit-box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.3);\n-moz-box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.3);\nbox-shadow: 0px 0px 8px rgba(0, 0, 0, 0.3);\n}\ninput    {\nwidth:375px;\ndisplay:block;\nborder: 1px solid #999;\nheight: 25px;\n-webkit-box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.3);\n-moz-box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.3);\nbox-shadow: 0px 0px 8px rgba(0, 0, 0, 0.3);\n}\ninput.submit {\nwidth:100px;\nposition:absolute;\nright:20px;\nbottom:20px;\nbackground:#09C;\ncolor:#fff;\nfont-family: Tahoma, Geneva, sans-serif;\nheight:30px;\n-webkit-border-radius: 15px;\n-moz-border-radius: 15px;\nborder-radius: 15px;\nborder: 1p solid #999;\n}\ninput.submit:hover {\nbackground:#fff;\ncolor:#09C;\n}\n.menudes {\nposition: relative;\noverflow: hidden;\nwidth: 70%;\nmargin: 10px auto 10px;\nborder-radius: 8px;\nbackground: #025BA3;\ntext-align:center;\nfont-family: Tahoma, Geneva, sans-serif;\n}\n.menudes a {\ndisplay: inline-block;\nwidth: 15%; /* 100% dividido por el n\xfamero de elementos del men\xfa */\nbox-sizing: border-box;\npadding: 10px 5px;\ncolor: #fff;\ntext-decoration: none;\n}\n.marca {\nposition: absolute;\nbottom: 4px;\nleft: -12.5%; /* Al menos 1/2 del ancho de cada enlace */\nwidth: 12.5%; /* 1/2 del ancho de cada enlace */\nheight: 4px;\nbackground: #fff;\ntransition: 0.5s ease-in-out; \n}\n.menudes a:nth-child(1):hover ~ .marca {\nleft: 15.25%; /* 1/4 Ancho del enlace */\n}\n.menudes a:nth-child(2):hover ~ .marca {\nleft: 36.25%; /* 1/4 Ancho del enlace + 1 vez ancho enlace */\n}\n.menudes a:nth-child(3):hover ~ .marca {\nleft: 49.25%; /* 1/4 Ancho del enlace + 2 veces ancho enlace */\n}\n.menudes a:nth-child(4):hover ~ .marca {\nleft: 69.5%; /* 1/4 Ancho del enlace + 3 veces ancho enlace */\n}\n</style>\n<script language="javascript">\nfunction checkEmail() {\n\tvar email = document.getElementById(\'email\');\n\tvar sub = document.getElementById(\'submit\');\n\tvar filter = /^([a-zA-Z0-9_\\.\\-])+\\@(([a-zA-Z0-9\\-])+\\.)+([a-zA-Z0-9]{2,4})+$/;\n\tif (!filter.test(email.value)) {\n\t\tsub.disabled=true;\n\t\talert(\'Please provide a valid email address\');\n\t\temail.focus;\n\t\treturn false;\n\t}else{\n\t\tsub.disabled=false;\n\t}\n}\n</script>\n</head>\n<body>\n<div class="menudes">\n<a href="/formtest/index">Inicio</a>\n<a href="/formtest/form">New Employee</a>\n<a href="/formtest/list">Employees</a>\n<a href="/formtest/contact">Contacto</a>\n<div class="marca"></div>\n</div>\n<form name="test" method="post" action="/formtest/submit">\n<div>\n<h1>Add a new Employee</h1>\n<label>\n<span>Name: </span><input id="name" type="text" name="name" />\n</label><br/>\n<label>\n<span>Email: </span><input id="email" type="text" name="email" onblur="javascript:checkEmail();" />\n</label><br/>\n<label>\n<span>Date of Birth: </span><input type="text" name="dof" placeholder="yyyy-mm-dd"/>\n</label><br/>\n<label>\n<span>Salary Amount: </span><input type="text" name="salario"/>\n</label><br/>\n<label>\n<span>Department: </span><select name="apartment"><option value="1">Administration</option><option value="2">Direction</option></select>\n</label>\n<br/><br/>\n<div align="center"><input type="submit" id="submit" name="submit" value="Save"/></div>\n</div>\n</form>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


