<%inherit file="/base/base.mako"/>\
<%def name="header()">Crea una nueva entrada:</%def>
%if hasattr(c,'contenido'):
  ${h.form_start(url(controller="contenido",action="guardar_contenido",id=c.contenido['id']))}
    Título de la entrada:
    ${h.text(name='titulo')} <br />
    Texto:
    ${h.textarea(name='texto', rows=10, cols = 40)} <br />
    ${h.submit(value='Guardar', name='commit')}
  ${h.form_end()}
%else:
  ${h.form_start(url(controller="contenido",action="guardar_contenido"))}
    Título de la entrada:
    ${h.text(name='titulo')} <br />
    Texto:
    ${h.textarea(name='texto', rows=10, cols = 40)} <br />
    ${h.submit(value='Guardar', name='commit')}
  ${h.form_end()}
%endif
