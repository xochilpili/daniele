#!/usr/bin/python
#
#
#  exercise connect mysql
############
import time
import datetime
from sqlalchemy import *
from datetime import datetime

engine = create_engine('mysql://root:x0chetzalt@localhost/testDaniele?charset=utf8&use_unicode=0', pool_recycle=3600)
connection = engine.connect()
result = engine.execute("""select nombre,email,date_format(fech_birth,'%%d/%%m/%%Y') as fech_birth,salario from cat_employees""")
for row in result:
	print "Name: {} | Email: {} | Salario {}Eur | Birth : {}.".format(row['nombre'],row['email'],row['salario'],row['fech_birth'])
connection.close()
