import unittest
from mockito import when, verify, unstub, mock

from src.negocio.Banco import Banco
from src.negocio.Cliente import Cliente
from src.negocio.ContaEspecial import ContaEspecial
from src.negocio.ContaPoupanca import ContaPoupanca

from src.exceptions.AtualizacaoNaoRealizadaException import AtualizacaoNaoRealizadaException
from src.exceptions.ContaNaoEncontradaException import ContaNaoEncontradaException
from src.exceptions.ClienteNaoCadastradoException import ClienteNaoCadastradoException
from src.exceptions.ContaJaAssociadaException import ContaJaAssociadaException
from src.exceptions.RenderBonusContaEspecialException import RenderBonusContaEspecialException
from src.exceptions.RenderJurosPoupancaException import RenderJurosPoupancaException
from src.exceptions.ValorInvalidoException import ValorInvalidoException


class test_banco_com_mockito(unittest.TestCase):

    def setUp(self):
        self.repo_clientes = mock()
        self.repo_contas = mock()
        self.banco = Banco(self.repo_clientes, self.repo_contas)

    def tearDown(self):
        unstub()

    def test_atualizar_cliente_falha_lanca_excecao(self):
        cliente = Cliente("João", "123")
        when(self.repo_clientes).atualizar(cliente).thenReturn(False)

        with self.assertRaises(AtualizacaoNaoRealizadaException):
            self.banco.atualizar_cliente(cliente)

        verify(self.repo_clientes).atualizar(cliente)

    def test_creditar_valor_negativo(self):
        conta = mock()
        with self.assertRaises(ValorInvalidoException):
            self.banco.creditar(conta, -1)

    def test_debitar_valor_negativo(self):
        conta = mock()
        with self.assertRaises(ValorInvalidoException):
            self.banco.debitar(conta, -10)

    def test_render_bonus_conta_nao_existe(self):
        conta = ContaEspecial("001", 100)
        when(self.repo_contas).existe("001").thenReturn(False)

        with self.assertRaises(ContaNaoEncontradaException):
            self.banco.render_bonus(conta)

        verify(self.repo_contas).existe("001")

    def test_render_bonus_conta_nao_especial(self):
        conta = ContaPoupanca("002", 100)
        when(self.repo_contas).existe("002").thenReturn(True)

        with self.assertRaises(RenderBonusContaEspecialException):
            self.banco.render_bonus(conta)

    def test_render_juros_conta_nao_existe(self):
        conta = ContaPoupanca("003", 100)
        when(self.repo_contas).existe("003").thenReturn(False)

        with self.assertRaises(ContaNaoEncontradaException):
            self.banco.render_juros(conta)

    def test_render_juros_conta_nao_poupanca(self):
        conta = ContaEspecial("004", 100)
        when(self.repo_contas).existe("004").thenReturn(True)

        with self.assertRaises(RenderJurosPoupancaException):
            self.banco.render_juros(conta)

    def test_associar_conta_ja_associada_a_outro_cliente(self):
        cliente1 = Cliente("João", "111")
        cliente2 = Cliente("Maria", "222")

        cliente1.adicionar_conta("001")

        when(self.repo_clientes).getIterator().thenReturn(iter([cliente1, cliente2]))
        when(self.repo_clientes).procurar("222").thenReturn(cliente2)

        conta = mock()
        when(conta).getNumero().thenReturn("001")
        when(self.repo_contas).procurar("001").thenReturn(conta)

        with self.assertRaises(ContaJaAssociadaException):
            self.banco.associar_conta("222", "001")

    def test_associar_conta_cliente_nao_existe(self):
        conta = mock()
        when(conta).getNumero().thenReturn("001")

        when(self.repo_contas).procurar("001").thenReturn(conta)
        when(self.repo_clientes).procurar("999").thenReturn(None)

        with self.assertRaises(ClienteNaoCadastradoException):
            self.banco.associar_conta("999", "001")

    def test_get_instance_retorna_singleton(self):
        b1 = Banco.get_instance()
        b2 = Banco.get_instance()
        self.assertIs(b1, b2)


def runBancoMockitoTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_banco_com_mockito)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == "__main__":
    runBancoMockitoTests()
