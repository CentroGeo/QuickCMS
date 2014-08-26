<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
  <head>
    <title>QuicCMS</title>
    ##${h.stylesheet_link('/quick.css')}
  </head>

  <body>
    <div class="content">
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
