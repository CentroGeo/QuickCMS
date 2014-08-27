<%inherit file="/base/base.mako"/>\
<%def name="header()">Información del usuario:</%def>
Nombre de usuario: ${c.usuario.username} </br>
Correo electrónico: ${c.usuario.email} </br>
