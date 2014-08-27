<%inherit file="/base/base.mako"/>\
<%def name="header()">Entrada:</%def>
<p>Título: ${c.contenido.titulo}</p>
<p>Texto: ${c.contenido.texto}</p>
<p>Creado por: ${c.contenido.usuario.username}</p>
<p>Fecha de creación: ${c.contenido.creado}</p>
<p><a href="${h.url(controller ='contenido', action='index')}">Todas las entradas</a>
<p><a href="${h.url(controller ='usuarios', action='home')}">Home</a>
