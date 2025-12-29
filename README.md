# PP - 2025.2 - Atividade 1 - Cobrindo código do banco

---

## Testes Automatizados

Os testes foram implementados utilizando:

* **unittest**
* **pytest**
* **Mockito (mockito-python)** para simulação de dependências

Todos os testes passam corretamente.

### Executar todos os testes

```bash
python -m test.tudo_test
```

---

## Análise de Cobertura

| Arquivo                       | Cover    |
| ----------------------------- | -------- |
| Banco.py                      | 64%      |
| Conta.py                      | 92%      |
| ContaAbstrata.py              | 93%      |
| ContaEspecial.py              | 100%     |
| ContaImposto.py               | 100%     |
| ContaPoupanca.py              | 100%     |
| Cliente.py                    | 100%     |
| RepositorioContasArquivoDB.py | 28%      |
| RepositorioContasArray.py     | 100%     |

> **Observação:**
> A ferramenta **mutmut** apresentou incompatibilidade com projetos estruturados no padrão `src/`, abortando a execução durante a instrumentação do código.
