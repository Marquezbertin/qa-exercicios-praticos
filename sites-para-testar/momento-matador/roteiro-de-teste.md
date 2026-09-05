# Momento Matador - Roteiro de Testes

**Empresa:** Momento Matador (fictícia)
**Sistema:** Loja de games
**QA responsável:** __________
**Data:** __________

---

## Casos de Teste

### CT-01 - Listagem de todos os jogos
| Campo | Valor |
|---|---|
| Passos | Página carregada sem filtro |
| Resultado esperado | 6 jogos exibidos, cada um com nome, plataforma, preço e desconto quando houver |

Status: [ ] Passou [ ] Falhou

### CT-02 - Busca exata
| Campo | Valor |
|---|---|
| Passos | Busque "God of War" |
| Resultado esperado | Somente God of War aparece |

Status: [ ] Passou [ ] Falhou

### CT-03 - Busca case-insensitive (minúsculas)
| Campo | Valor |
|---|---|
| Passos | Busque `zelda` (minúsculas) e depois `ZELDA` (maiúsculas) |
| Resultado esperado | Ambos encontram "The Legend of Zelda" (busca não pode diferenciar maiúsculas/minúsculas) |

Status: [ ] Passou [ ] Falhou

### CT-04 - Busca parcial
| Campo | Valor |
|---|---|
| Passos | Busque "war" |
| Resultado esperado | God of War aparece |

Status: [ ] Passou [ ] Falhou

### CT-05 - Busca sem resultados
| Campo | Valor |
|---|---|
| Passos | Busque "existsNothing" |
| Resultado esperado | Grid vazio, sem mensagem de erro (avaliar UX) |

Status: [ ] Passou [ ] Falhou

### CT-06 - Preço com desconto (Zelda)
| Campo | Valor |
|---|---|
| Passos | Observe o card do Zelda (desconto 10%) |
| Resultado esperado | 299,90 - 10% = **R$ 269,91**. O preço antigo (299,90) é exibido riscado |

Status: [ ] Passou [ ] Falhou

### CT-07 - Preço com desconto (Cyberpunk)
| Campo | Valor |
|---|---|
| Passos | Observe o card do Cyberpunk (desconto 20%) |
| Resultado esperado | 199,90 - 20% = **R$ 159,92** |

Status: [ ] Passou [ ] Falhou

### CT-08 - Promoção "até hoje"
| Campo | Valor |
|---|---|
| Passos | Leia o aviso no topo ("desconto de 10% no jogo Zelda **até hoje**!"); desconfie da data |
| Resultado esperado | A promoção deve expirar na data anunciada. Após o prazo, o desconto não deve mais ser aplicado. **Confira se existe alguma lógica de data** |

Status: [ ] Passou [ ] Falhou

### CT-09 - Adicionar ao carrinho e total
| Campo | Valor |
|---|---|
| Passos | Compre 1 Zelda e 1 Elden Ring |
| Resultado esperado | Total = 269,91 + 299,90 = **R$ 569,81** |

Status: [ ] Passou [ ] Falhou

### CT-10 - Múltiplas unidades
| Campo | Valor |
|---|---|
| Passos | Compre 2x Stardew Valley (24,99) |
| Resultado esperado | Total = **R$ 49,98** |

Status: [ ] Passou [ ] Falhou

### CT-11 - Feedback ao comprar
| Campo | Valor |
|---|---|
| Passos | Clique em "Comprar" |
| Resultado esperado | Algum feedback visual (mudança no carrinho OU confirmação) de que o item foi adicionado |

Status: [ ] Passou [ ] Falhou

---

## Checklist

- [ ] Busca funcional (exata, parcial, case-insensitive)
- [ ] Cálculo de desconto correto
- [ ] Promoção com prazo respeitando a data
- [ ] Total do carrinho consistente
- [ ] Feedback ao adicionar item

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |