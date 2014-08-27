"""The application's model objects"""
from quickcms.model.meta import Session, Base
from quickcms.model.contenidos import Contenido
from quickcms.model import *


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
