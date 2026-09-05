# Gabarito - Exercício 01 - Calculadora de descontos

> Consulte APENAS depois de tentar.

## Bugs intencionais

### BUG 1 - Preço ZERO não é rejeitado (Severidade: Alta)
- **Onde:** `if preco < 0` na função `calcular_desconto`.
- **Regra:** "Preço deve ser maior que zero".
- **Esperado:** `preco == 0` deve lançar `ValueError`.
- **Obtido:** `calcular_desconto(0, 10)` retorna `0.0` sem erro.
- **Como ver:** O caso `(0, 10, None)` do teste falha (`FALHOU ... obteve=0.0`).

### BUG 2 - O caso de teste original validava comportamento incorreto (Severidade: Média)
- **Onde:** O teste original trazia `(0, 10, 0)` como "esperado", ou seja, tratava o preço zero como aceitável.
- **Observação:** Aqui mora uma lição importante: **o teste herdava a especificação errada**. O QA precisa questionar a especificação, não apenas fazer o teste passar.

### Observação
- O limite de desconto (máx. 50%) está implementado corretamente (`> 50` lança erro); não é bug.

---

## Correção sugerida
```python
if preco <= 0:
    raise ValueError("Preço inválido")
```