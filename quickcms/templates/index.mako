<%inherit file="/base/base.mako"/>\

<%def name="header()">Bienvenido</%def>

%if request.environ.get('repoze.who.identity') is not None:
    %if 'admin' in c.nombres_grupos:
        <p><a href="${h.url(controller ='contenido', action='crear_post')}">Crear entrada</a>
    %endif
    <p><a href="${h.url(controller ='contenido', action='index')}">Ver entradas</a>
%endif
