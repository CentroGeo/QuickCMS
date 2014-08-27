<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
  <head>
    <title>QuicCMS</title>
    ##${h.stylesheet_link('/quick.css')}
  </head>

  <body>
    <div class="content">
        <div>
            %if request.environ.get('repoze.who.identity') is not None:
                <p>Usuario: ${request.environ.get('repoze.who.identity')['user'].username}</p>
                <p><a href="${h.url(controller ='login', action='logout_handler')}">Salir</a>
                </p>
            %else:
                <p><a href="${h.url(controller ='login', action='login')}">Entrar</a>
                <p><a href="${h.url(controller ='usuarios', action='crear')}">Regístrate</a>
            %endif
        </div>
        <h1 class="main">${self.header()}</h1>
        % if session.has_key('flash'):
           <div id="flash"><p>${session.get('flash')}</p></div>
        <%
            del session['flash']
            session.save()
        %>
        % endif
        ${next.body()}\
        <p class="footer">
          QuickCMS
        </p>
    </div>
  </body>
</html>
