# Gabarito - Exercício 06 - Validador de CPF

> Consulte APENAS depois de tentar. Execute `exercicio-06-cpf.py` e observe que CPFs válidos conhecidos falham.

## Bugs intencionais

### BUG 1 - Peso do 2º dígito verificador errado (Severidade: Alta)
- **Onde:** No 2º cálculo, o loop usa `(10 - i)`, mas o algoritmo oficial usa pesos **11, 10, 9, ..., 2** (ou seja, `(11 - i)`).
- **Esperado:** `529.982.247-25` e `123.456.789-09` retornam True.
- **Obtido:** Ambos retornam False (e `52998224725` sem máscara também falha).
- **Correção:** `soma += int(cpf[i]) * (11 - i)`.

### Observações
- O 1º dígito verificador usa pesos 10..2: `(10 - i)` está correto.
- A rejeição de "todos os dígitos iguais" (`cpf == cpf[0] * 11`) e a limpeza de não-dígitos estão corretas.

---

## Verificação extra para QA
- Confirme que `529.982.247-25` (válido) é aceito e que `123.456.789-10` (inválido) é rejeitado.
- Teste também: somente dígitos, comprimento 11, dígitos iguais e um CRLF/branco no fim (o `re.sub` cuida disso).
- **Lição:** um erro de "off-by-one" num peso de validação é um clássico; sempre rode teste com valores conhecidos antes de confiar numa função crítica.