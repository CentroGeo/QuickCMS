from pylons import request, response, session, tmpl_context, config

#from repoze.what.plugins.pylonshq import ActionProtector, ControllerProtector
from quickcms.lib.auth import ActionProtector
from repoze.what.predicates import is_user, has_permission, in_group

from quickcms.lib.base import BaseController, render

class RootController(BaseController):
    def index(self):
        return render('index.mako')

    @ActionProtector(is_user('test'))
    def user(self):
        return render('loggedin.mako')

    @ActionProtector(is_user('nottest'))
    def notuser(self):
        return render('loggedin.mako')

    @ActionProtector(in_group('admin'))
    def admin(self):
        return render('loggedin.mako')

    @ActionProtector(has_permission('edit'))
    def edit(self):
        return render('loggedin.mako')
