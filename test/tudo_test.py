from test.conta_test import runContaTests
from test.conta_abstrata_test import runContaAbstrataTests
from test.conta_especial_test import runContaEspecialTests
from test.conta_imposto_test import runContaImpostoTests
from test.conta_poupanca_test import runContaPoupancaTests

from test.cliente_test import runClienteTests

from test.banco_test_mockito import runBancoMockitoTests
from test.mockito_database_test import runMockitoTests as runMockitoDatabaseTests

from test.repositorio_contas_array_test import runRepositorioContasArrayTests
from test.test_repositorio_contas_arquivo_db_mockito import runRepositorioContasMockitoTests


def runAllTests():
    print("-*"*30, "\n", "Rodando testes da classe Conta\n", "-*"*30)
    runContaTests()
    print("-*"*30, "\n", "Fim dos testes da classe Conta\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes da classe Conta Abstrata\n", "-*"*30)
    runContaAbstrataTests()
    print("-*"*30, "\n", "Fim dos testes da classe Conta Abstrata\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes da classe Conta Especial\n", "-*"*30)
    runContaEspecialTests()
    print("-*"*30, "\n", "Fim dos testes da classe Conta Especial\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes da classe Conta Imposto\n", "-*"*30)
    runContaImpostoTests()
    print("-*"*30, "\n", "Fim dos testes da classe Conta Imposto\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes da classe Conta Poupança\n", "-*"*30)
    runContaPoupancaTests()
    print("-*"*30, "\n", "Fim dos testes da classe Conta Poupança\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes da classe Cliente\n", "-*"*30)
    runClienteTests()
    print("-*"*30, "\n", "Fim dos testes da classe Cliente\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes do Banco (Mockito)\n", "-*"*30)
    runBancoMockitoTests()
    print("-*"*30, "\n", "Fim dos testes do Banco (Mockito)\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes do Database (Mockito)\n", "-*"*30)
    runMockitoDatabaseTests()
    print("-*"*30, "\n", "Fim dos testes do Database (Mockito)\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes do Repositório (Array)\n", "-*"*30)
    runRepositorioContasArrayTests()
    print("-*"*30, "\n", "Fim dos testes do Repositório (Array)\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando testes do Repositório (Arquivo + DB + Mockito)\n", "-*"*30)
    runRepositorioContasMockitoTests()
    print("-*"*30, "\n", "Fim dos testes do Repositório (Arquivo + DB + Mockito)\n", "-*"*30, "\n")


if __name__ == '__main__':
    runAllTests()
