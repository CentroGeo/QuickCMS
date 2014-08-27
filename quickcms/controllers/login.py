from pylons import request, response, session, tmpl_context, config, url
from pylons.controllers.util import redirect

from quickcms.lib.base import BaseController, render
from quickcms.lib.helpers import flash

class LoginController(BaseController):
    def login(self):
        login_counter = request.environ['repoze.who.logins']
        if login_counter > 0:
            flash('Wrong credentials')
        tmpl_context.login_counter = login_counter
        tmpl_context.came_from = request.params.get('came_from') or url('/')
        return render('/derived/usuario/login.mako')

    def login_handler(self):
        pass

    def post_login(self):
        identity = request.environ.get('repoze.who.identity')
        came_from = str(request.params.get('came_from', '')) or url('/')
        if not identity:
            login_counter = request.environ['repoze.who.logins'] + 1
            redirect(url('/login', came_from=came_from, __logins=login_counter))
        redirect(came_from)

    def logout_handler(self):
        pass

    def post_logout(self):
        redirect('/')
