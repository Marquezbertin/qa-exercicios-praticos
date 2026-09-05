# TechStore - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes. Use para conferir se você encontrou os defeitos.

## Bugs presentes no site

### BUG 1 - Frete grátis com limite errado (Severidade: Média)
- **Onde:** `calcularFrete()` usa `sub >= 100`.
- **Esperado:** O banner anuncia "Frete grátis em compras ACIMA de R$ 100", ou seja, `sub > 100`. Uma compra de exatamente R$ 100,00 deveria cobrar R$ 15,00 de frete.
- **Obtido:** Compras de exatamente R$ 100,00 recebem frete grátis.
- **Como testar:** CT-03.

### BUG 2 - Cupom FRETEGRATIS adiciona valor ao total (Severidade: Alta)
- **Onde:** `descontoAplicado()` retorna `-frete` para o cupom FRETEGRATIS, mas `total = sub - desconto + frete`.
- **Conta:** sub=99,90, frete=15, desconto=-15 => total = 99,90 - (-15) + 15 = **R$ 129,90**.
- **Esperado:** 99,90 (frete zerado).
- **Como testar:** CT-05.

### BUG 3 - Banner vs. regra de cupom FRETEGRATIS não acumulável (Severidade: Baixa)
- **Onde:** O descriptor do cupom permite aplicar FRETEGRATIS após QA10 (substituindo). A regra de negócio diz que "FRETEGRATIS não pode ser combinado com QA10". O comportamento de substituir é ambíguo: não há aviso claro ao usuário.
- **Como testar:** CT-06.

### BUG 4 - Sem validação de estoque (Severidade: Média)
- **Onde:** `adicionarCarrinho()` aceita qualquer quantidade `>= 1`.
- **Esperado:** Deve haver um limite de estoque por produto (ex.: 10 unidades) com aviso ao usuário.
- **Obtido:** É possível comprar 999 ou 999999 unidades.
- **Como testar:** CT-09.

### BUG 5 - Campo de quantidade aceita valores inválidos com parse incoerente (Severidade: Média)
- **Onde:** `adicionarCarrinho()` usa `parseInt`, que aceita "3abc" como 3 e `2.9` como 2.
- **Esperado:** Entradas não numéricas ou fracionárias devem ser rejeitadas com mensagem clara.
- **Como testar:** CT-08.

### BUG 6 - Formatação monetária inconsistente (Severidade: Baixa)
- **Onde:** Preços no carrinho usam `toFixed(2)` apenas em alguns lugares; contador de itens não mostra valor total. Não há formatação BRL (R$ 1.234,56).
- **Exemplo:** R$ 4299.00 exibido como "R$ 4299.00" no subtotal da linha.

---

## O que o usuário deveria ter encontrado se testasse bem

1. Verificar sempre o caso-limite exato do frete (R$ 100,00).
2. Conferir a matemática do total (não confiar só no valor mostrado).
3. Testar combinação e troca de cupons.
4. Tentar quantidades absurdas e valores "sujos".
5. Comparar valor do catálogo vs valor cobrado.