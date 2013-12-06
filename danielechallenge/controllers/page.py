import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from danielechallenge.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PageController(BaseController):

    def view(self,id):
        # Return a rendered template
        #return render('/page.mako')
        # or, return a string
        c.title = 'Greetings'
    	c.heading = 'Sample Page'
    	c.content = "This is page %s"%id
    	return render('/derived/page/view.html')
