from pylons import response, url
from pylons.controllers.util import redirect

from repoze.what.plugins.quickstart import setup_sql_auth
from repoze.what.plugins import pylonshq

import quickcms.lib.helpers as h

from quickcms.model.meta import Session
from quickcms.model.auth import AuthUser, AuthGroup, AuthPermission

def add_auth(app, config):
   return setup_sql_auth(
       app, AuthUser, AuthGroup, AuthPermission, Session,
       login_handler = '/login/submit',
       logout_handler = '/logout',
       post_login_url = '/login/continue',
       post_logout_url = '/logout/continue',
       cookie_secret = 'my_secret_word',
       translations = {
           'user_name' : 'username',
           'groups' : 'auth_groups',
           'group_name' : 'name',
           'permissions' : 'auth_permissions',
           'permission_name' : 'name'
       }
   )

def redirect_auth_denial(reason):
    if response.status_int == 401:
        message = 'You are not logged in.'
        message_type = 'warning'
    else:
        message = 'You do not have the permissions to access this page.'
        message_type = 'error'

    #h.flash(message, message_type)
    redirect(url('/login', came_from=url.current()))

class ActionProtector(pylonshq.ActionProtector):
    default_denial_handler = staticmethod(redirect_auth_denial)
