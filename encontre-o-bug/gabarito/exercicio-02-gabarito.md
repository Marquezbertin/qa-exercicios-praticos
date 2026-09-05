# Gabarito - Exercício 02 - Sistema bancário

> Consulte APENAS depois de tentar.

## Bugs intencionais

### BUG 1 - Taxa de 2% cobrada do DESTINATÁRIO em vez do REMETENTE (Severidade: Alta)
- **Onde:** Linha `destino.depositar(valor - taxa)`.
- **Regra:** "A taxa deve ser cobrada do REMETENTE".
- **Esperado:** Remetente debita `valor + taxa`; destinatário recebe `valor`.
- **Obtido:** Remetente debita apenas `valor` (João: 2500 em vez de 2460) e o destinatário recebe `valor - taxa` (Maria: 2560 em vez de 2600). <br>
  O Teste 2 falha exatamente nesses valores.

### BUG 2 - Depósito permite valores negativos (Severidade: Média - latente)
- **Onde:** `ContaBancaria.depositar()` soma qualquer valor sem validar.
- **Esperado:** Depósito deve ser >= 0 (rejeitar negativos).
- **Obtido:** Um depósito de -100 reduziria o saldo. Não é exercitado pelos testes atuais (bug invisível = bug pior!).

### Observação
- Transferência para a mesma conta, saldo insuficiente, valor negativo e conta inexistente estão tratados corretamente.

---

## Correção sugerida
```python
# Remetente paga valor + taxa
total = valor + taxa
origem.sacar(total)
destino.depositar(valor)
```
E em `depositar`:
```python
if valor <= 0:
    raise ValueError("Depósito deve ser maior que zero")
```