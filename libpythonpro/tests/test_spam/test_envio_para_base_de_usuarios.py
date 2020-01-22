from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Eric', email='e.ericszcz@gmail.com'),
            Usuario(nome='Luciano', email='luciano@gmail.com')
        ],
        [
            Usuario(nome='Eric', email='e.ericszcz@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)

    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'e.ericszcz@gmail.com',
        "Curso Python pro",
        "Confira os módulos fantasticos"
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Eric', email='e.ericszcz@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        "Curso Python pro",
        "Confira os módulos fantasticos"
    )
    enviador.enviar.assert_called_once_with(
        'luciano@gmail.com',
        'e.ericszcz@gmail.com',
        "Curso Python pro",
        "Confira os módulos fantasticos"
    )
