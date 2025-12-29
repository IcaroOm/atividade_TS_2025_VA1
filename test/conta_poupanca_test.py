from src.negocio.ContaPoupanca import ContaPoupanca
from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException

import unittest


class test_conta_poupanca_numero(unittest.TestCase):
    def test_conta_poupanca_numero(self):
        conta = ContaPoupanca("123", 100.0)
        self.assertEqual(conta.getNumero(), "123", msg="O número da conta deveria ser 123")


class test_conta_poupanca_saldo_inicial(unittest.TestCase):
    def test_conta_poupanca_saldo_inicial(self):
        conta = ContaPoupanca("123", 100.0)
        self.assertEqual(conta.getSaldo(), 100.0, msg="O saldo inicial deveria ser 100.0")


class test_conta_poupanca_render_juros(unittest.TestCase):
    def test_conta_poupanca_render_juros(self):
        conta = ContaPoupanca("123", 100.0)

        conta.render_juros(0.1)

        self.assertEqual(conta.getSaldo(), 110.0, msg="O saldo deveria ser 110.0 após juros")


class test_conta_poupanca_render_juros_zero(unittest.TestCase):
    def test_conta_poupanca_render_juros_zero(self):
        conta = ContaPoupanca("123", 100.0)

        conta.render_juros(0.0)

        self.assertEqual(conta.getSaldo(), 100.0, msg="O saldo não deveria mudar com taxa zero")


class test_conta_poupanca_render_juros_multiplos(unittest.TestCase):
    def test_conta_poupanca_render_juros_multiplos(self):
        conta = ContaPoupanca("123", 100.0)

        conta.render_juros(0.1)   # +10
        conta.render_juros(0.2)   # +22

        self.assertEqual(conta.getSaldo(), 132.0)


class test_conta_poupanca_get_tipo(unittest.TestCase):
    def test_get_tipo(self):
        conta = ContaPoupanca("123", 100.0)
        self.assertEqual(conta.get_tipo(), "poupanca")


def runContaPoupancaTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_poupanca_numero)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_poupanca_saldo_inicial))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_poupanca_render_juros))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_poupanca_render_juros_zero))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_poupanca_render_juros_multiplos))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_poupanca_get_tipo))

    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    runContaPoupancaTests()
