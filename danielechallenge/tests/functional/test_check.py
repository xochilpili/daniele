from danielechallenge.tests import *

class TestCheckController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='check', action='index'))
        # Test response...
