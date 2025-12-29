from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.negocio.ContaImposto import ContaImposto

import unittest


class test_conta_imposto_debito(unittest.TestCase):
    def test_conta_imposto_debito(self):
        conta = ContaImposto("123", 100.0)
        conta.debitar(50.0)
        self.assertEqual(conta.getSaldo(), 49.81, msg="O saldo da conta deveria ser 49.81")


class test_conta_imposto_debito_saldo_insuficiente(unittest.TestCase):
    def test_conta_imposto_debito_saldo_insuficiente(self):
        conta = ContaImposto("123", 100.0)
        with self.assertRaises(SaldoInsuficienteException):
            conta.debitar(150.0)


class test_conta_imposto_numero(unittest.TestCase):
    def test_conta_imposto_numero(self):
        conta = ContaImposto("123", 100.0)
        self.assertEqual(conta.getNumero(), "123", msg="O número da conta deveria ser 123")


class test_conta_imposto_get_tipo(unittest.TestCase):
    def test_get_tipo(self):
        conta = ContaImposto("123", 100.0)
        self.assertEqual(conta.get_tipo(), "imposto")


class test_conta_imposto_cpmf_aplicado_corretamente(unittest.TestCase):
    def test_cpmf_aplicado_corretamente(self):
        conta = ContaImposto("123", 100.0)

        valor = 10.0
        imposto_esperado = valor * ContaImposto.CPMF
        saldo_esperado = 100.0 - (valor + imposto_esperado)

        conta.debitar(valor)

        self.assertAlmostEqual(conta.getSaldo(), saldo_esperado, places=5)


class test_conta_imposto_multiplos_debitos(unittest.TestCase):
    def test_multiplos_debitos(self):
        conta = ContaImposto("123", 200.0)

        conta.debitar(50.0)
        saldo_apos_primeiro = conta.getSaldo()

        conta.debitar(25.0)
        imposto = 25.0 * ContaImposto.CPMF
        saldo_esperado = saldo_apos_primeiro - (25.0 + imposto)

        self.assertAlmostEqual(conta.getSaldo(), saldo_esperado, places=5)


def runContaImpostoTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_debito)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_debito_saldo_insuficiente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_numero))

    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_get_tipo))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_cpmf_aplicado_corretamente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_multiplos_debitos))

    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    runContaImpostoTests()
