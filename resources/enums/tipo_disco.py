
from django.utils.translation import gettext_lazy as _



class TipoDisco:
    MECANICO = 'A'
    SOLIDO = 'B'
    NULO = 'B'
    OPCIONES = [
        (MECANICO, _('MECANICO')),
        (SOLIDO, _('SOLIDO')),
        (NULO, _('NULO')),
    ]


class TiempoFuncionamiento:
    UNO_DOS = '1-2'
    DOS_TRES = '2-3'
    TRES_CUATRO = '3-4'
    CUATRO_CINCO = '4-5'
    CINCO_MAS = '5+'

    OPCIONES = [
        (UNO_DOS, _('1-2 Años')),
        (DOS_TRES, _('2-3 Años')),
        (TRES_CUATRO, _('3-4 Años')),
        (CUATRO_CINCO, _('4-5 Años')),
        (CINCO_MAS, _('5+ Años')),
    ]
