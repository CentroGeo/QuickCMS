<% messages = h.flash.pop_messages() %>
% if messages:
<div class="flash">
    % for message in messages:
      <p class="${message.category}">${message}
    % endfor
</div>
% endif

  <form action="${h.url('/login/submit', came_from=tmpl_context.came_from, __logins=tmpl_context.login_counter)}" method="POST">
    <label for="login">Username:<input type="text" id="login" name="login" /><br />
    <label for="password">Password:<input type="password" id="password" name="password" />
    <input type="submit" value="Login" />
  </form>