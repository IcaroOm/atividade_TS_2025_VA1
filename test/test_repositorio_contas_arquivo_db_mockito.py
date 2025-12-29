import unittest
from mockito import when, unstub

from src.dados.RepositorioContasArquivoDB import RepositorioContasArquivoDB
from src.negocio.Conta import Conta
from src.negocio.ContaEspecial import ContaEspecial
from src.negocio.ContaPoupanca import ContaPoupanca


class test_inserir_conta(unittest.TestCase):
    def test_inserir_conta(self):

        rep = RepositorioContasArquivoDB()

        conta = Conta("123", 100)
        when(rep).inserir(conta).thenReturn(True)

        result = rep.inserir(conta)

        self.assertEqual(result, True)

        unstub()


class test_procurar_conta(unittest.TestCase):
    def test_procurar_conta(self):

        rep = RepositorioContasArquivoDB()

        conta = ContaEspecial("321", 200)
        when(rep).procurar("321").thenReturn(conta)

        result = rep.procurar("321")

        self.assertEqual(result, conta)

        unstub()


class test_remover_conta(unittest.TestCase):
    def test_remover_conta(self):

        rep = RepositorioContasArquivoDB()

        when(rep).remover("999").thenReturn(True)

        result = rep.remover("999")

        self.assertEqual(result, True)

        unstub()


class test_atualizar_conta(unittest.TestCase):
    def test_atualizar_conta(self):

        rep = RepositorioContasArquivoDB()

        conta = ContaPoupanca("555", 500)
        when(rep).atualizar(conta).thenReturn(True)

        result = rep.atualizar(conta)

        self.assertEqual(result, True)

        unstub()


class test_existe_conta(unittest.TestCase):
    def test_existe_conta(self):

        rep = RepositorioContasArquivoDB()

        when(rep).existe("123").thenReturn(True)

        result = rep.existe("123")

        self.assertEqual(result, True)

        unstub()


class test_get_iterator(unittest.TestCase):
    def test_get_iterator(self):

        rep = RepositorioContasArquivoDB()

        contas_mock = [
            {"numero": "1", "saldo": 10},
            {"numero": "2", "saldo": 20}
        ]

        when(rep).get_iterator().thenReturn(iter(contas_mock))

        result = list(rep.get_iterator())

        self.assertEqual(result, contas_mock)

        unstub()


def runRepositorioContasMockitoTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_inserir_conta)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_procurar_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_remover_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_atualizar_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_existe_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_get_iterator))

    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == "__main__":
    runRepositorioContasMockitoTests()
