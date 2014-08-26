from quickcms.tests import *

class TestContenidoController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='contenido', action='index'))
        # Test response...
