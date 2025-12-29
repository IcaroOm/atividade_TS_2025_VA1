from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.negocio.ContaEspecial import ContaEspecial

import unittest


class test_conta_especial_debito(unittest.TestCase):
    def test_conta_especial_debito(self):
        conta = ContaEspecial("123", 100.0)
        conta.debitar(50.0)
        self.assertEqual(conta.getSaldo(), 50.0, msg="O saldo da conta deveria ser 50.0")


class test_conta_especial_debito_saldo_insuficiente(unittest.TestCase):
    def test_conta_especial_debito_saldo_insuficiente(self):
        conta = ContaEspecial("123", 100.0)
        with self.assertRaises(SaldoInsuficienteException):
            conta.debitar(150.0)


class test_conta_especial_numero(unittest.TestCase):
    def test_conta_especial_numero(self):
        conta = ContaEspecial("123", 100.0)
        self.assertEqual(conta.getNumero(), "123", msg="O número da conta deveria ser 123")


class test_conta_especial_saldo_inicial_negativo(unittest.TestCase):
    def test_conta_especial_saldo_inicial_negativo(self):
        conta = ContaEspecial("123", -100.0)
        self.assertEqual(conta.getSaldo(), 0.0, msg="O saldo da conta deveria ser 0.0")
        

class test_conta_especial_bonus_inicial(unittest.TestCase):
    def test_bonus_inicial_zero(self):
        conta = ContaEspecial("123", 100.0)
        self.assertEqual(
            conta.getBonus(),
            0.0,
            msg="O bônus inicial da conta especial deve ser 0.0"
        )


class test_conta_especial_creditar_bonus(unittest.TestCase):
    def test_creditar_adiciona_bonus(self):
        conta = ContaEspecial("123", 100.0)
        conta.creditar(100.0)

        self.assertEqual(
            conta.getSaldo(),
            200.0,
            msg="O saldo deve ser atualizado corretamente ao creditar"
        )

        self.assertAlmostEqual(
            conta.getBonus(),
            1.0,
            msg="O bônus deve ser 1% do valor creditado"
        )


class test_conta_especial_bonus_acumulado(unittest.TestCase):
    def test_bonus_acumula_em_multiplos_creditos(self):
        conta = ContaEspecial("123", 100.0)
        conta.creditar(100.0)
        conta.creditar(200.0)

        self.assertAlmostEqual(
            conta.getBonus(),
            3.0,
            msg="O bônus deve acumular corretamente após múltiplos créditos"
        )


class test_conta_especial_render_bonus(unittest.TestCase):
    def test_render_bonus(self):
        conta = ContaEspecial("123", 100.0)
        conta.creditar(100.0)  # bônus = 1.0
        conta.renderbonus()

        self.assertAlmostEqual(
            conta.getSaldo(),
            201.0,
            msg="O saldo deve incluir o bônus após renderização"
        )

        self.assertEqual(
            conta.getBonus(),
            0.0,
            msg="O bônus deve ser zerado após renderização"
        )


class test_conta_especial_set_bonus(unittest.TestCase):
    def test_set_bonus(self):
        conta = ContaEspecial("123", 100.0)
        conta.setBonus(10.0)

        self.assertEqual(
            conta.getBonus(),
            10.0,
            msg="O método setBonus deve atualizar corretamente o bônus"
        )


class test_conta_especial_tipo(unittest.TestCase):
    def test_get_tipo(self):
        conta = ContaEspecial("123", 100.0)
        self.assertEqual(
            conta.get_tipo(),
            "especial",
            msg="O tipo da conta especial deve ser 'especial'"
        )


def runContaEspecialTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_debito)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_debito_saldo_insuficiente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_numero))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_saldo_inicial_negativo))

    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_bonus_inicial))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_creditar_bonus))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_bonus_acumulado))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_render_bonus))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_set_bonus))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_tipo))

    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    runContaEspecialTests()
