# FoodGo - Roteiro de Testes

**Empresa:** FoodGo Brasil (fictícia)
**Sistema:** Delivery de comida
**QA responsável:** __________
**Data:** __________

---

## Casos de Teste

### CT-01 - Pedido sem itens
| Campo | Valor |
|---|---|
| Pré-condição | Nenhum item selecionado |
| Passos | Preencha CEP válido e clique em "Finalizar pedido" sem escolher itens |
| Resultado esperado | Erro "selecione pelo menos um item" |

Status: [ ] Passou [ ] Falhou

### CT-02 - Pedido mínimo (R$ 15,00)
| Campo | Valor |
|---|---|
| Passos | Selecione apenas "Refrigerante Lata" (R$ 6,50) e tente finalizar com CEP válido |
| Resultado esperado | Erro "pedido mínimo de R$ 15,00" |

Status: [ ] Passou [ ] Falhou

### CT-03 - CEP inválido (menos de 8 dígitos)
| Campo | Valor |
|---|---|
| Passos | CEP `1234` e `1234567` |
| Resultado esperado | Erro "CEP inválido" |

Status: [ ] Passou [ ] Falhou

### CT-04 - CEP fora da área de entrega
| Campo | Valor |
|---|---|
| Passos | CEP `20000-000` (prefixo 20000 não está nas faixas) |
| Resultado esperado | Erro "não entregamos neste CEP" |

Status: [ ] Passou [ ] Falhou

### CT-05 - CEP dentro da área (faixa 1)
| Campo | Valor |
|---|---|
| Passos | CEP `01310-100` -> prefixo 01310, taxa R$ 5,90 |
| Resultado esperado | Taxa de entrega R$ 5,90 exibida no resumo |

Status: [ ] Passou [ ] Falhou

### CT-06 - Cálculo do total básico
| Campo | Valor |
|---|---|
| Passos | Selecione X-Burger (22,90) e Refrigerante (6,50). CEP 01310-100 |
| Resultado esperado | Subtotal 29,40; taxa 5,90; total = 29,40 + 5,90 = **R$ 35,30** |

Status: [ ] Passou [ ] Falhou

### CT-07 - Combo Burger (10% de desconto)
| Campo | Valor |
|---|---|
| Passos | Clique no "Combo Burger". Itens adicionados: X-Burger + X-Salada (22,90 + 25,90 = 48,80). Sem taxa (CEP da faixa 1, 5,90) |
| Resultado esperado | Desconto = 4,88. Total = 48,80 - 4,88 + 5,90 = **R$ 49,82** |

Status: [ ] Passou [ ] Falhou

### CT-08 - Remover item do combo após aplicar o combo
| Campo | Valor |
|---|---|
| Passos | Aplique o Combo Burger. Depois CLIQUE no "X-Salada" para remover (pedido fica só com X-Burger, 22,90) |
| Resultado esperado | Desconto deve recalcular para o que realmente está no pedido (itens removidos não podem gerar desconto). Nenhum desconto indevido |

Status: [ ] Passou [ ] Falhou

### CT-09 - Pagamento em dinheiro com valor menor que o total
| Campo | Valor |
|---|---|
| Passos | Total R$ 35,30. Pague em dinheiro R$ 20,00 |
| Resultado esperado | Erro pedindo valor pago maior ou igual ao total |

Status: [ ] Passou [ ] Falhou

### CT-10 - Pagamento em dinheiro com troco (vírgula)
| Campo | Valor |
|---|---|
| Passos | Total R$ 35,30. Pague em dinheiro **49,90** (com vírgula) |
| Resultado esperado | Troco a devolver = 49,90 - 35,30 = **R$ 14,60** |

Status: [ ] Passou [ ] Falhou

### CT-11 - Horário fora de funcionamento
| Campo | Valor |
|---|---|
| Passos | Com o site aberto verifique o comportamento; para testar o bloqueio, altere a hora do sistema ou verifique a lógica: funciona apenas entre 11h e 23h |
| Resultado esperado | Fora do horário, o pedido não é enviado e uma mensagem de aviso aparece |

Status: [ ] Passou [ ] Falhou

### CT-12 - Total nunca negativo
| Campo | Valor |
|---|---|
| Passos | Tente combinar quantos descontos possíveis com o menor pedido (ex: combo Doce - itens 4 e 5 = 52,90) e observe |
| Resultado esperado | Total sempre >= R$ 0,00 |

Status: [ ] Passou [ ] Falhou

---

## Checklist

- [ ] Pedido mínimo validado
- [ ] Desconto só incide sobre itens realmente no pedido
- [ ] Taxa de entrega correta por faixa de CEP
- [ ] CEP fora da área bloqueia o pedido
- [ ] Troco em dinheiro calculado corretamente (inclusive com vírgula)
- [ ] Bloqueio por horário de funcionamento
- [ ] Total nunca negativo

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |