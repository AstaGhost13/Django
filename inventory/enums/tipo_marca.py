from django.utils.translation import gettext_lazy as _

class TipoMarca:
    PERIFERICOS = 'A'
    EOFICINA = 'B'
    ECOMPUTO = 'C'
    OTROS = 'D'

    OPCIONES = [
        (PERIFERICOS, _('PERIFERICOS')),
        (EOFICINA, _('EQUIPOS DE OFICINA')),
        (ECOMPUTO, _('EQUIPOS DE COMPUTO')),
        (OTROS, _('OTROS')),
    ]