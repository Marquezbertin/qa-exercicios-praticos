# TechStore - Roteiro de Testes

**Empresa:** TechStore S.A. (fictícia)
**Sistema:** Loja virtual - carrinho de compras
**QA responsável:** __________
**Data:** __________

---

## Como usar este roteiro

1. Abra `index.html` no navegador.
2. Execute cada caso de teste abaixo.
3. Registre o resultado obtido e o status (Passou / Falhou / Bloqueado).
4. Para cada falha, documente em um formulário de bug (modelo na raiz do projeto).
5. Ao terminar, confira com o arquivo `gabarito-bugs.md`.

---

## Casos de Teste

### CT-01 - Adicionar produto ao carrinho
| Campo | Valor |
|---|---|
| Pré-condição | Carrinho vazio |
| Passos | 1. Clique em "+" do Notebook . 2. Clique em "Adicionar ao Carrinho". 3. Abra o carrinho. 4. Clique em "-" até zerar |
| Resultado esperado | Contador do carrinho = 1; valor = R$ 4.299,00 (preço promocional) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-02 - Valor promocional vs preço cheio
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Adicione 1 unidade do Notebook (promoção 4299,00 vs 4599,00) e 1 do Mouse (sem promoção, 99,90). Confira o subtotal |
| Resultado esperado | Subtotal = 4299,00 + 99,90 = R$ 4.398,90 |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-03 - Frete grátis (limite de R$ 100)
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | A) Adicione quantidade suficiente para totalizar exatamente R$ 100,00. B) totalizar R$ 99,99. C) totalizar R$ 100,01 |
| Resultado esperado | A) Como o banner diz "acima de R$ 100", exatamente R$ 100,00 deve COBRAR frete de R$ 15. B e C seguem a regra |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-04 - Cupom QA10 (10% de desconto)
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Adicione 1 Mouse (99,90). Aplique o cupom QA10 |
| Resultado esperado | Desconto = R$ 9,99. Total = 99,90 - 9,99 + frete 15 = R$ 104,91 |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-05 - Cupom FRETEGRATIS
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Adicione 1 Mouse (99,90). Aplique FRETEGRATIS |
| Resultado esperado | Total = 99,90 (sem frete). Nada deve ser adicionado ao total |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-06 - Troca de cupom (QA10 -> FRETEGRATIS)
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Aplique QA10 e depois FRETEGRATIS no mesmo carrinho |
| Resultado esperado | Somente 1 cupom ativo. Total reflete apenas o frete grátis |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-07 - Cupom inválido
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Digite QA11 e clique em aplicar |
| Resultado esperado | Mensagem "Cupom inválido" em vermelho, sem desconto aplicado |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-08 - Quantidade inválida no campo numérico
| Campo | Valor |
|---|---|
| Pré-condição | DevTools aberto (F12) |
| Passos | Digite 0, um número negativo ou letras no campo de quantidade e clique em "Adicionar ao Carrinho" |
| Resultado esperado | Sistema rejeita com mensagem clara, sem alterar o carrinho |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-09 - Quantidade muito alta
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Digite 999 no campo de quantidade de um produto e adicione (verifique limite de estoque) |
| Resultado esperado | Sistema valida limite de estoque ou apresenta aviso |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-10 - Total nunca negativo
| Campo | Valor |
|---|---|
| Pré-condição | DevTools aberto (F12) |
| Passos | Aplique QA10 em um carrinho com total pequeno (ex.: R$ 5,00) e observe o total |
| Resultado esperado | Total nunca fica negativo (valor mínimo R$ 0,00) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-11 - Carrinho vazio
| Campo | Valor |
|---|---|
| Pré-condição | Sem itens |
| Passos | Abra o carrinho vazio e clique em "Finalizar Compra" |
| Resultado esperado | Mensagem "Seu carrinho está vazio" sem confirmar pedido |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

---

## Checklist de verificação

- [ ] Preço exibido no catálogo = preço cobrado no carrinho
- [ ] Frete grátis respeita o limite exato descrito no banner (> R$ 100)
- [ ] Desconto de cupom incide somente sobre o subtotal
- [ ] Cupom FRETEGRATIS não altera o subtotal nem adiciona valor
- [ ] Contador do carrinho reflete o total de itens corretamente
- [ ] Botão "+" e "-" funcionam e respeitam mínimo de 1
- [ ] Finalizar exibe o mesmo total mostrado no resumo
- [ ] Mensagens de erro são visíveis e amigáveis

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |
| 2 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |
| 3 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |