# FoodGo - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes.

## Bugs presentes no site

### BUG 1 - Remover item do combo mantém o desconto integral (Severidade: Alta)
- **Onde:** `descontoCombo()` sempre calcula 10% sobre a soma dos itens do combo, mesmo que um item tenha sido removido do pedido depois.
- **Esperado:** Desconto deve refletir apenas os itens que estão realmente no carrinho.
- **Obtido:** Combo Burger aplicado e depois X-Salada removido: o pedido tem apenas X-Burger (22,90), mas o desconto continua de 4,88. Cliente paga a menos.
- **Como testar:** CT-08.

### BUG 2 - Troco em dinheiro ignora centavos com vírgula (Severidade: Média)
- **Onde:** `parseFloat(document.getElementById("troco").value || "0")`.
- **Esperado:** Valor digitado `49,90` = R$ 49,90; troco = R$ 14,60.
- **Obtido:** `parseFloat("49,90")` = 49; troco = 49,00 - 35,30 = R$ 13,70 (errado por R$ 0,90).
- **Como testar:** CT-10.

### BUG 3 - Bloqueio de horário só é verificado no clique (Severidade: Baixa/Usabilidade)
- **Onde:** O aviso de fechado só aparece no `confirmarPedido()`; se o restaurante fecha com a página aberta, o resumo não sinaliza.
- **Esperado:** Aviso visível mesmo antes de finalizar.
- **Como testar:** CT-11.

### BUG 4 - Desconto pode superar o subtotal de itens fora do combo (Severidade: Média)
- **Onde:** `total = sub - desc + taxa`, com `sub` incluindo itens que não fazem parte do combo. O desconto é calculado sobre a soma dos itens do combo, porém `sub` pode conter itens avulsos -- a matemática está correta, mas confirme o caso em que o desconto calculado fica maior do que o valor cobrado dos itens do combo (cliente pode pagar menos do que o devido em certas combinações).

---

## Principais lições deste exercício
- Descontos precisam ser revalidados a cada mudança no carrinho (estado consistente).
- Formatação de moeda local (vírgula) é fonte clássica de bugs.
- Testar sempre "alteração de estado": aplicar e depois remover partes da ação.
- Validar regras de negócio (pedido mínimo, cobertura de CEP, horário) em cada caminho.