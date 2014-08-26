<%inherit file="/base/base.mako"/>\
<%def name="header()">Contenidos:</%def>
<ul>
    %for item in c.contenidos:
        <ul>
            <li>Título: ${item.titulo} </li>
            <li>Usuario: ${item.usuario.nombre_usuario} </li>
            <li>Creado en: ${item.creado} </li>
            <li>Contenido: ${item.texto} </li>
        </ul>


    %endfor

</ul>
