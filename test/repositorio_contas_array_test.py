import unittest

from src.dados.RepositorioContasArray import RepositorioContasArray
from src.negocio.Conta import Conta
from src.negocio.ContaEspecial import ContaEspecial


class test_repositorio_contas_array_inserir(unittest.TestCase):

    def test_inserir_conta_com_sucesso(self):
        rep = RepositorioContasArray()
        conta = Conta("1", 100)

        result = rep.inserir(conta)

        self.assertTrue(result)
        self.assertEqual(rep.procurar("1"), conta)

    def test_inserir_conta_duplicada(self):
        rep = RepositorioContasArray()
        conta = Conta("1", 100)

        rep.inserir(conta)
        result = rep.inserir(conta)

        self.assertFalse(result)


class test_repositorio_contas_array_procurar(unittest.TestCase):

    def test_procurar_conta_inexistente(self):
        rep = RepositorioContasArray()

        result = rep.procurar("999")

        self.assertIsNone(result)


class test_repositorio_contas_array_remover(unittest.TestCase):

    def test_remover_conta_existente(self):
        rep = RepositorioContasArray()
        conta = Conta("1", 100)

        rep.inserir(conta)
        result = rep.remover("1")

        self.assertTrue(result)
        self.assertIsNone(rep.procurar("1"))

    def test_remover_conta_inexistente(self):
        rep = RepositorioContasArray()

        result = rep.remover("999")

        self.assertFalse(result)

    def test_remover_troca_posicao(self):
        rep = RepositorioContasArray()
        conta1 = Conta("1", 100)
        conta2 = Conta("2", 200)

        rep.inserir(conta1)
        rep.inserir(conta2)

        rep.remover("1")

        self.assertEqual(rep.procurar("2"), conta2)
        self.assertIsNone(rep.procurar("1"))


class test_repositorio_contas_array_atualizar(unittest.TestCase):

    def test_atualizar_conta_existente(self):
        rep = RepositorioContasArray()
        conta = Conta("1", 100)
        nova = Conta("1", 500)

        rep.inserir(conta)
        result = rep.atualizar(nova)

        self.assertTrue(result)
        self.assertEqual(rep.procurar("1").getSaldo(), 500)

    def test_atualizar_conta_inexistente(self):
        rep = RepositorioContasArray()
        conta = Conta("1", 100)

        result = rep.atualizar(conta)

        self.assertFalse(result)


class test_repositorio_contas_array_existe(unittest.TestCase):

    def test_existe_conta(self):
        rep = RepositorioContasArray()
        conta = Conta("1", 100)

        rep.inserir(conta)

        self.assertTrue(rep.existe("1"))

    def test_existe_conta_inexistente(self):
        rep = RepositorioContasArray()

        self.assertFalse(rep.existe("999"))


class test_repositorio_contas_array_iterator(unittest.TestCase):

    def test_get_iterator(self):
        rep = RepositorioContasArray()
        conta1 = ContaEspecial("1", 100)
        conta2 = Conta("2", 200)

        rep.inserir(conta1)
        rep.inserir(conta2)

        contas = list(rep.get_iterator())

        self.assertIn(conta1, contas)
        self.assertIn(conta2, contas)
        self.assertEqual(len(contas), 2)


class test_repositorio_contas_array_resize(unittest.TestCase):

    def test_array_aumenta_quando_cheio(self):
        rep = RepositorioContasArray()

        for i in range(100):
            rep.inserir(Conta(str(i), i))

        self.assertTrue(rep.inserir(Conta("101", 101)))
        self.assertIsNotNone(rep.procurar("101"))


def runRepositorioContasArrayTests():
    suite = unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_repositorio_contas_array_inserir))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_repositorio_contas_array_procurar))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_repositorio_contas_array_remover))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_repositorio_contas_array_atualizar))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_repositorio_contas_array_existe))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_repositorio_contas_array_iterator))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_repositorio_contas_array_resize))

    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == "__main__":
    runRepositorioContasArrayTests()
