import logging
import danielechallenge.lib.helpers as h

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from danielechallenge.lib.base import BaseController, render
from sqlalchemy import *

log = logging.getLogger(__name__)

class FormtestController(BaseController):

    def index(self):
	str=""
	return render('/derived/page/index.html', extra_vars={'result' : str})

    def contact(self):
	return render('/derived/page/contact.html')

    def form(self):
        # Return a rendered template
        #return render('/formtest.mako')
        # or, return a string
        return render('/derived/page/simpleform.html')

    def submit(self):
	str=""
	nom=request.params['name']
	mail=request.params['email']
	dep=request.params['apartment']
	fech=request.params['dof']
	sal=request.params['salario']
	engine = create_engine('mysql://root:x0chetzalt@localhost/testDaniele?charset=utf8&use_unicode=0', pool_recycle=3600)
        connection = engine.connect()
        result = engine.execute(""" insert into cat_employees values (null,%s,%s,%s,%s,%s,%s);""",dep,nom,mail,"password",fech,sal)
	#return 'Your data is: %s' % nom + ' email: %s ' % mail + ' department: %s ' % dep + ' fech: %s ' % fech + ' Salary: %s ' % sal
	str="New employee added!"
	return render('/derived/page/index.html', extra_vars={'result' : str})

    def list(self):
	str=""
	counter=1
	engine = create_engine('mysql://root:x0chetzalt@localhost/testDaniele?charset=utf8&use_unicode=0', pool_recycle=3600)
	connection = engine.connect()
	result = engine.execute("""select cat_employees.nombre,cat_employees.email,date_format(cat_employees.fech_birth, '%%d/%%m/%%Y') as fech_birth, cat_employees.salario, cat_apartments.description from cat_employees inner join cat_apartments on cat_employees.id_apartment=cat_apartments.id_apartment order by cat_employees.nombre""")
	for row in result:
		str += h.literal('<tr><td> %s ' % row['nombre'] + '</td><td> %s ' % row['email']+'</td><td> %s' % row['description'] + '<td> %s ' % row['fech_birth'] + '</td><td> %s &#8364;' % row['salario'] + '</td></tr>') 
	counter +=1
	connection.close()
	return render('/derived/page/list.html', extra_vars={'rows' : str})
