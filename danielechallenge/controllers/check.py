import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from danielechallenge.lib.base import BaseController, render

log = logging.getLogger(__name__)

class CheckController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/check.mako')
        # or, return a string
        return 'Hello World'
    def hi(self):
	return 'hi there!'
