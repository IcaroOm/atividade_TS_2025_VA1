from src.negocio.Cliente import Cliente
from src.exceptions.ClienteJaPossuiContaException import ClienteJaPossuiContaException
from src.exceptions.ClienteNaoPossuiContaException import ClienteNaoPossuiContaException

import unittest


class test_cliente_cpf(unittest.TestCase):
    def test_cliente_cpf(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_cpf(), "12345678900", msg="O CPF do cliente deveria ser 12345678900")


class test_cliente_nome(unittest.TestCase):
    def test_cliente_nome(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_nome(), "João", msg="O nome do cliente deveria ser João")


class test_cliente_contas(unittest.TestCase):
    def test_cliente_contas(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_contas(), [], msg="O cliente não deveria possuir contas")


class test_cliente_adicionar_conta(unittest.TestCase):
    def test_cliente_adicionar_conta(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        self.assertEqual(cliente.get_contas(), ["123"], msg="O cliente deveria possuir a conta 123")


class test_cliente_remover_conta(unittest.TestCase):
    def test_cliente_remover_conta(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        cliente.remover_conta("123")
        self.assertEqual(cliente.get_contas(), [], msg="O cliente não deveria possuir contas")


class test_cliente_remover_todas_as_contas(unittest.TestCase):
    def test_cliente_remover_todas_as_contas(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        cliente.adicionar_conta("456")
        cliente.remover_todas_as_contas()
        self.assertEqual(cliente.get_contas(), [], msg="O cliente não deveria possuir contas")


class test_cliente_adicionar_conta_duplicada(unittest.TestCase):
    def test_adicionar_conta_duplicada(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")

        with self.assertRaises(ClienteJaPossuiContaException):
            cliente.adicionar_conta("123")


class test_cliente_remover_conta_inexistente(unittest.TestCase):
    def test_remover_conta_inexistente(self):
        cliente = Cliente("João", "12345678900")

        with self.assertRaises(ClienteNaoPossuiContaException):
            cliente.remover_conta("999")


class test_cliente_procurar_conta_existente(unittest.TestCase):
    def test_procurar_conta_existente(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")

        index = cliente.procurar_conta("123")
        self.assertEqual(index, 0)


class test_cliente_procurar_conta_inexistente(unittest.TestCase):
    def test_procurar_conta_inexistente(self):
        cliente = Cliente("João", "12345678900")

        index = cliente.procurar_conta("999")
        self.assertEqual(index, -1)


class test_cliente_consultar_numero_conta(unittest.TestCase):
    def test_consultar_numero_conta(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        cliente.adicionar_conta("456")

        self.assertEqual(cliente.consultar_numero_conta(1), "456")


class test_cliente_setters(unittest.TestCase):
    def test_set_nome_e_cpf(self):
        cliente = Cliente("João", "12345678900")

        cliente.set_nome("Maria")
        cliente.set_cpf("00011122233")

        self.assertEqual(cliente.get_nome(), "Maria")
        self.assertEqual(cliente.get_cpf(), "00011122233")


class test_cliente_eq_true(unittest.TestCase):
    def test_cliente_eq_true(self):
        c1 = Cliente("João", "123")
        c2 = Cliente("Maria", "123")

        self.assertEqual(c1, c2)


class test_cliente_eq_false_tipo_diferente(unittest.TestCase):
    def test_cliente_eq_false_tipo_diferente(self):
        cliente = Cliente("João", "123")

        self.assertNotEqual(cliente, "123")


class test_cliente_str(unittest.TestCase):
    def test_cliente_str(self):
        cliente = Cliente("João", "123")
        cliente.adicionar_conta("456")

        texto = str(cliente)

        self.assertIn("João", texto)
        self.assertIn("123", texto)
        self.assertIn("456", texto)


def runClienteTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_cpf)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_nome))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_contas))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_adicionar_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_remover_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_remover_todas_as_contas))

    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_adicionar_conta_duplicada))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_remover_conta_inexistente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_procurar_conta_existente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_procurar_conta_inexistente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_consultar_numero_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_setters))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_eq_true))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_eq_false_tipo_diferente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_str))

    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    runClienteTests()
