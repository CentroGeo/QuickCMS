from quickcms.tests import *

class TestUsuariosController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='usuarios', action='index'))
        # Test response...
