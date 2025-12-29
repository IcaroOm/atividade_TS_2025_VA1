import unittest

from src.negocio.ContaAbstrata import ContaAbstrata
from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException


class ContaFake(ContaAbstrata):

    def debitar(self, valor: float):
        if self.getSaldo() < valor:
            raise SaldoInsuficienteException(self.getNumero(), self.getSaldo())
        self.setSaldo(self.getSaldo() - valor)

    def get_tipo(self) -> str:
        return "fake"


class test_conta_abstrata_getters_setters(unittest.TestCase):

    def test_get_numero(self):
        conta = ContaFake("123", 100)
        self.assertEqual(conta.getNumero(), "123")

    def test_set_numero(self):
        conta = ContaFake("123", 100)
        conta.setNumero("999")
        self.assertEqual(conta.getNumero(), "999")

    def test_get_saldo(self):
        conta = ContaFake("123", 100)
        self.assertEqual(conta.getSaldo(), 100)

    def test_set_saldo(self):
        conta = ContaFake("123", 100)
        conta.setSaldo(500)
        self.assertEqual(conta.getSaldo(), 500)


class test_conta_abstrata_creditar(unittest.TestCase):

    def test_creditar_valor_positivo(self):
        conta = ContaFake("123", 100)
        conta.creditar(50)
        self.assertEqual(conta.getSaldo(), 150)

    def test_creditar_valor_zero_nao_altera(self):
        conta = ContaFake("123", 100)
        conta.creditar(0)
        self.assertEqual(conta.getSaldo(), 100)

    def test_creditar_valor_negativo_nao_altera(self):
        conta = ContaFake("123", 100)
        conta.creditar(-10)
        self.assertEqual(conta.getSaldo(), 100)


class test_conta_abstrata_debitar(unittest.TestCase):

    def test_debitar_valor_valido(self):
        conta = ContaFake("123", 100)
        conta.debitar(40)
        self.assertEqual(conta.getSaldo(), 60)

    def test_debitar_valor_maior_que_saldo(self):
        conta = ContaFake("123", 100)
        with self.assertRaises(SaldoInsuficienteException):
            conta.debitar(200)


class test_conta_abstrata_eq(unittest.TestCase):

    def test_contas_com_mesmo_numero_sao_iguais(self):
        c1 = ContaFake("123", 100)
        c2 = ContaFake("123", 999)
        self.assertEqual(c1, c2)

    def test_contas_com_numeros_diferentes_nao_sao_iguais(self):
        c1 = ContaFake("123", 100)
        c2 = ContaFake("456", 100)
        self.assertNotEqual(c1, c2)

    def test_eq_com_tipo_diferente(self):
        conta = ContaFake("123", 100)
        self.assertFalse(conta == "123")


def runContaAbstrataTests():
    suite = unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_abstrata_getters_setters))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_abstrata_creditar))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_abstrata_debitar))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_abstrata_eq))
    
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == "__main__":
    runContaAbstrataTests()
