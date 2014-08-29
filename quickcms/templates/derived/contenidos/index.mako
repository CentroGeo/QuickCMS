<%inherit file="/base/base.mako"/>\
<%def name="header()">Contenidos:</%def>

    %for item in c.contenidos:
        <ul>
            <li>Título: ${item.titulo}
              <a href="${h.url(controller ='contenido', action='crear_post',id=item.id)}">Editar</a>
            </li>
            <li>Usuario: ${item.usuario.username} </li>
            <li>Creado en: ${item.creado} </li>
            <li>Contenido: ${item.texto} </li>
        </ul>


    %endfor

<p><a href="${h.url(controller ='usuarios', action='home')}">Home</a>
