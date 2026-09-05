# Gabarito - Exercício 03 - Carrinho de compras

> Consulte APENAS depois de tentar. Execute `exercicio-03-carrinho.py` e observe a falha no Teste 4.

## Bugs intencionais

### BUG 1 - Frete grátis no limite errado (Severidade: Alta)
- **Onde:** `if self.subtotal() > 100` em `frete()`.
- **Regra:** "Frete é grátis para pedidos ACIMA de R$ 100,00" -- iguais a R$ 100,00 PAGAM frete. (R$ 100,00 é o caso-limite inferior da regra "acima de".)
- **Esperado:** Subtotal exatamente R$ 100,00 => frete R$ 15,00.
- **Obtido:** Um subtotal de R$ 100,00 paga frete R$ 15,00, resultando em total de R$ 105,00 no Teste 4 (esperado R$ 90,00 com o cupom). **Observe: o teste falha precisamente porque o limite de frete está errado.**

### BUG 2 - Componente `FRETEGRATIS` pode não acumular desconto de forma transparente (Severidade: Baixa)
- **Onde:** Em `total()`, `FRETEGRATIS` zera o frete. **Se o pedido já teria frete grátis (< 100 é o único caso que cobra), o cupom não tem efeito -- e nada avisa o usuário.**
- **Observável:** Com subtotal R$ 30,00 e cupom FRETEGRATIS, o total é R$ 30,00 (parece que funcionou), mas com subtotal R$ 150,00 (frete já 0) o cupom simplesmente não faz nada.

### BUG 3 - Cupom aceito sem distinção de caixa (Severidade: Baixa)
- **Onde:** `aplicar_cupom` compara exatamente (maiúsculas). Digitar `qa10` minúsculo deveria ser normalizado (#aplicar `qa10` lança "Cupom inválido"). Código de cupom normalmente é case-insensitive.

---

## Correções sugeridas
1. `frete()`: usar `> 100` (regra "acima de 100") OU `>= 100` (regra "a partir de 100") -- **confirme com o Product Owner qual é a regra certa**; o gatilho é a regra, não o código.
2. Normalizar o cupom com `.upper()`.
3. Informar ao usuário quando o cupom não teve efeito.