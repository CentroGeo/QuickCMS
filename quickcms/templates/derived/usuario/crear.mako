<%inherit file="/base/base.mako"/>\

<%def name="header()">Nuevo usuario:</%def>

${h.form_start(url(controller="usuarios",action="guardar_usuario"))}
  Nombre de usuario:
  ${h.text(name='nombre_usuario')} <br />
  Correo electrónico:
  ${h.text(name='email')} <br />
  ${h.submit(value='Guardar', name='commit')}
${h.form_end()}
