# Hotel Reserva Fácil - Roteiro de Testes

**Empresa:** Reserva Fácil LTDA (fictícia)
**Sistema:** Reservas de hotel
**QA responsável:** __________
**Data:** __________

---

## Casos de Teste

### CT-01 - Busca com datas vazias
| Campo | Valor |
|---|---|
| Pré-condição | Limpe os campos de data |
| Passos | Clique em "Buscar quartos" |
| Resultado esperado | Mensagem pedindo as datas; nenhum quarto é exibido |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-02 - Check-out antes do check-in
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Check-in 10/09, check-out 08/09 |
| Resultado esperado | Mensagem de erro "check-out deve ser posterior" |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-03 - Check-out no MESMO dia do check-in
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Check-in = check-out = amanhã |
| Resultado esperado | Rejeitado (estadia mínima é 1 noite; "0 noite(s)" não é uma estadia válida) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-04 - Check-in em data passada
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Digite uma check-in de ontem |
| Resultado esperado | Rejeitado com mensagem clara |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-05 - Busca válida e preço calculado
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Check-in amanhã, check-out em 3 noites, 2 hóspedes |
| Resultado esperado | Mostra quartos; "X noite(s): R$ Y" = preço/noite x noites |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-06 - Promoção da 7ª noite grátis
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Check-in amanhã, check-out em **7 noites**, 2 hóspedes no Standard (R$ 250/noite) |
| Resultado esperado | O resumo anuncia "7ª noite grátis". Total esperado = 6 x 250 = **R$ 1.500,00** (7ª noite sem cobrança) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-07 - Indisponibilidade por conflito de reserva
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Pesquise o período 10/09 a 12/09 (Quarto Standard l id 1 já reservado 20/09-25/09; Standard Duplo id 2 reservado 10/09-12/09). Teste: período 10/09-12/09 deve mostrar Standard Duplo como indisponível |
| Resultado esperado | Quatro indisponível naquele período exibe "Indisponível no período" |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-08 - Capacidade de hóspedes
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Busque 6 hóspedes |
| Resultado esperado | Só a Suíte Presidencial (cap 5... verifique) — na verdade, verifique: quartos que não comportam 6 hóspedes devem exibir "Capacidade insuficiente" |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-09 - Modal: nome em branco
| Campo | Valor |
|---|---|
| Pré-condição | Pesquise um quarto disponível e clique em "Reservar" |
| Passos | Deixe nome vazio, e-mail válido, confirme |
| Resultado esperado | Mensagem de erro; reserva não confirmada |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-10 - Modal: e-mail inválido
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Teste os e-mails: `maria`, `maria@`, `maria@site`, `a@b.c`, `maria@site.com` |
| Resultado esperado | Formatos claramente inválidos rejeitados; `maria@site.com` aceito |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-11 - Modal: hóspedes acima da capacidade
| Campo | Valor |
|---|---|
| Pré-condição | Abra modal do Standard (cap 2) |
| Passos | Digite 3 hóspedes e confirme |
| Resultado esperado | Erro "capacidade excedida" |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-12 - Confirmar reserva duas vezes (duplo clique)
| Campo | Valor |
|---|---|
| Pré-condição | Modal aberto com dados válidos |
| Passos | Clique em "Confirmar reserva" MUITO RÁPIDO, duas vezes seguidas |
| Resultado esperado | Apenas UMA reserva é criada (sem duplicidade) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-13 - Após confirmar, quarto fica indisponível
| Campo | Valor |
|---|---|
| Pré-condição | Confirme uma reserva |
| Passos | Faça uma nova busca no MESMO período |
| Resultado esperado | Quarto recém-reservado aparece indisponível |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

---

## Checklist

- [ ] Datas são validadas (passado, invertidas, mesma data)
- [ ] Promoção anunciada é refletida no preço
- [ ] Preço total = preço/noite x noites
- [ ] Conflitos de reserva bloqueiam o quarto
- [ ] Capacidade de hóspedes respeitada na busca e no modal
- [ ] Campos do modal validados
- [ ] Nenhuma reserva duplicada

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |