<%inherit file="/base/base.mako"/>\

<%def name="header()">Nuevo usuario:</%def>

${h.form_start(url(controller="usuarios",action="guardar_usuario"))}
  Nombre de usuario:
  ${h.text(name='username')} <br />
  Correo electrónico:
  ${h.text(name='email')} <br />
  Contraseña:
  ${h.password(name='password')} <br />
  ${h.submit(value='Guardar', name='commit')}
${h.form_end()}
